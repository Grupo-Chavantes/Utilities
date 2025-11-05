class Supplier < ApplicationRecord
  validates :tax_id_number, presence: true, uniqueness: true, length: { maximum: 14 }
  validates :legal_name, presence: true, on: :update, length: { maximum: 150 }
end
