class CreateSipefInferences < ActiveRecord::Migration[8.1]
  def change
    create_table :sipef_inferences do |t|
      t.integer :status, null: false, default: 0

      t.timestamps
    end
  end
end
