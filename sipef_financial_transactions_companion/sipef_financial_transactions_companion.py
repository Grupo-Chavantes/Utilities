#!/user/bin/env python3

"""sipef_financial_transactions_companion

Deterministically infer and fill in the columns
OperacaoID, Classif.Pagto, Tipo Fornecedor, Class.Fornecedor and DocTipo
of the SIPEF financial transactions spreadsheet.
"""

import errno, logging, sys
from pathlib import Path

import pandas

from mappings.sipef import COD_HISTORICO_TO_DOCTIPO


def read_spreadsheet() -> pandas.DataFrame:
    in_filepath = Path.cwd() / "0200 - Movimentação financeira.xlsx"

    if not in_filepath.exists():
        raise FileNotFoundError

    return pandas.read_excel(in_filepath, sheet_name=0)


def infer_and_fill_columns(data_frame: pandas.DataFrame) -> pandas.DataFrame:
    data_frame["DocTipo"] = data_frame["Cod. Historico"].apply(
        lambda x: COD_HISTORICO_TO_DOCTIPO.get(to_int_safe(x), 5)) # 5 = Outros

    return data_frame.drop(columns=["DESPESA CÓDIGO", "Cod. Historico"])


def to_int_safe(value: any) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0


def export_spreadsheet(data_frame: pandas.DataFrame) -> None:
    out_filepath = Path.cwd() / "0200 - Movimentação financeira - SFTC.xlsx"
    data_frame.to_excel(out_filepath, index=False)


if __name__ == "__main__":
    try:
        logging.basicConfig(
            filename=Path.cwd() / "errors.txt",
            level=logging.ERROR,
            format="%(asctime)s %(levelname)s: %(message)s",
        )

        export_spreadsheet(
            infer_and_fill_columns(
                read_spreadsheet()
            )
        )
    except FileNotFoundError as e:
        logging.error("Expected spreadsheet not found.", exc_info=True)
        sys.exit(errno.ENOENT)
    except Exception as e:
        logging.error("Error processing the spreadsheet.", exc_info=True)
        sys.exit(1)
