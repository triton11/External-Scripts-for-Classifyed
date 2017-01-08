class WelcomeController < ApplicationController

	def index
		
		render 'welcome'
	end
	def view
		@words = params[:fname] + " "
		@score = 2.459316805
		ave = 0
		count = 0

		arr = []

		@words.split(" ").each do |item|
			count += 1
			uned = item.capitalize
			line = Line.find_by(word: uned)
			if line != nil
				ave += line.weight
			end
		end
		@score += 4*(ave/count)


		
		render 'results'
	end
end
