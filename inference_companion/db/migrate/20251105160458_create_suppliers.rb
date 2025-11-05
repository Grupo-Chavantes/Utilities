class CreateSuppliers < ActiveRecord::Migration[8.1]
  def change
    create_table :suppliers do |t|
      t.string :tax_id_number, limit: 14, null: false
      t.string :legal_name, limit: 150
      t.text :cnaes_keywords
      t.json :cnpjws

      t.timestamps
    end
    add_index :suppliers, :tax_id_number, unique: true
  end
end
