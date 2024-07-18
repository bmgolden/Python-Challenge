# Python-Challenge
Brendan Golden 
Python Challenge Read Me 

After examining this module, I devised a plan to replicate the desired output. I exhausted multiple resources to devise a script for both files that correctly presents the required variables and formats for the datasets. I began by examining material from earlier lectures covering the most effective way to import and read the CSV files while being able to extrapolate and print the header from the rest of the imported file. After completing the first step I directed my attention to reproducing the provided financial analysis. I used previously acquired knowledge from self-study, and this class to incorporate the use of for loops and conditional statements to deduce the variables needed in the script for total months along with total profit and loss. The next component proved more challenging as you had to inject the script with multiple syntaxes to find the desired value for the average change across the quarters. Using the included XPert learning assistant and some minor interjections from Chat GPT, I achieved the necessary value using techniques relative to list and list commands, variable declaration, and loops. After calculating the numerical value, I partnered with a couple of my classmates, Chris and Nick, as we found the best possible method for extracting the greatest profit increase and greatest profit decrease, and the associated months using complex index properties and basic manipulation. The second dataset started similarly as we calculated the total number of votes as the total months in the first. For the next, and most crucial part of the analysis, we relied on three different mediums to replicate the desired analysis. We first relied on previous knowledge, second, we went to office hours and were pointed in the right direction by the great TA, and finally, we used Chat GPT and the XPert AI to deduce the necessary for loop integration with the dictionary, along with a couple of dictionary methods, concerning keys, values, and items that were not covered in class. The penultimate step was to correctly implement the f-string method, with braces, and replicate the desired analysis to match the one provided in the module. The final step was to complete the requirements and be able to execute the script without any bugs or hindrances, comment out the code explaining the methodology, and simultaneously print out the analysis portion, as a text file, to the necessary folder on our respective computers and upload to GitHub. 

Taking a deeper dive into the code itself, we aimed to present a streamlined script reaching the requirements given to us in the module. We tried to present our code in the most logical, sequential, and concise way possible to attain the output. The PyBank and PyPoll files start similarly with variable declaration, transitioning into reading the CSV files and correctly skipping the header of the datasets. Next, for the bank data, we implemented a for loop and calculated the total months and profit, while adding necessary information to lists that we would need for future calculations.  The toughest part was to calculate, and store, each change in the profit and loss section to a list, while calculating the average change and rounding the number. The last part was relatively straightforward as we found the max and min values and used indexed to extrapolate the months. For the PyPoll data, after the first part, we implemented conditionals and a mix of dictionaries to add each vote to the respective candidate and store it in a list. Next, we printed the necessary output and used another for loop, with dictionary methods, to accurately calculate the percentage of the vote each candidate received. In the end, we declared the winner and printed out the results. 

