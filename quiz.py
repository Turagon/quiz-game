import requests as r
import json
import html
import random 

url_em = "https://opentdb.com/api.php?amount=1&difficulty=easy&type=multiple"
url_eb = "https://opentdb.com/api.php?amount=1&difficulty=easy&type=boolean"
url_mm = "https://opentdb.com/api.php?amount=1&difficulty=medium&type=multiple"
url_mb = "https://opentdb.com/api.php?amount=1&difficulty=medium&type=boolean"
url_hm = "https://opentdb.com/api.php?amount=1&difficulty=hard&type=multiple"
url_hb = "https://opentdb.com/api.php?amount=1&difficulty=hard&type=boolean"
choice = {"em" : url_em, "eb" : url_eb, "mm" : url_mm, "mb" : url_mb, "hm" : url_hm, "hb" : url_hb}
n = 1 # the question number
correct_count = 0
incorrect_count = 0
ask = input("Do you like to play quiz? Enter y to start : ")
if ask.lower() == "y" :
	while True :
		x = input("Please select difficulty : h = Hard, m = Medium, e = Easy : ") # x = difficulty
		if x.lower() in ["e", "m", "h"] :
			y = input("Please select quiz type : m = Multiple choice, b = True/False : ")
			while True :
				if y.lower() not in ["m", "b"] :
					y = input("Type is invalid value, select again : ")
					continue
				else :
					 break
		else :
			print("Difficulty is invalid value")
			continue

		while True :
			url = choice[x + y]
			quiz = r.get(url)
			if quiz.status_code != 200 :
				input("Http get problem, sorry, please press enter to try again : ")
			else :
				break

		print("The ", n, " question is :")
		question = json.loads(quiz.text)
		print(html.unescape(question["results"][0]["question"]))
		c_ans = html.unescape(question["results"][0]["correct_answer"])
		inc_ans = html.unescape(question["results"][0]["incorrect_answers"])
		inc_ans.append(c_ans)
		random.shuffle(inc_ans)
		an = 1
		for answers in inc_ans :
			print(an, ". ", answers )
			an += 1
				
		user_ans = input("Please choose your answer : ")
		while True :
			try :
				user_ans == int(user_ans)
				if int(user_ans) > 0 and int(user_ans) <= len(inc_ans) :
					break
				else :
					user_ans = input("Invalid value, please input again : ")
			except :
				user_ans = input("Invalid value, please input again : ")

		user_ans = int(user_ans)
		if inc_ans[(user_ans-1)] == c_ans :
			print("Congratualtion!")
			correct_count += 1
		else :
			print("Sorry, the correct answer is ", c_ans)
			incorrect_count += 1
		print("Your correct answers are :", correct_count, "\n", "Your incorrect_count are :", incorrect_count)

		again = input("If you like to play again, input y : ")
		if again != "y" :
			print("Thanks for playing, bye bye.")
			break
		n += 1
else :
	print("OK, see you.")
		

