class SipefInference < ApplicationRecord
  has_one_attached :input_file
  has_one_attached :output_file

  validates :input_file, presence: true

  after_create do
    InferSipefCodesJob.perform_later(id)
  end

  enum :status, { awaiting: 0, processing: 1, processed: 2, failed: 3 }

  def humanize_status
    {
      awaiting: "Aguardando Processamento",
      processing: "Processando",
      processed: "Processado",
      failed: "Processamento Falhou"
    }[status.to_sym]
  end
end
