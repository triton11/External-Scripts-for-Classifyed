class CreateLines < ActiveRecord::Migration
  def change
    create_table :lines do |t|
      t.string :word
      t.float :weight

      t.timestamps null: false
    end
  end
end
