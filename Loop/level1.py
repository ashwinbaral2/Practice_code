# PRACTICE QUESTIONS — Nested If / Conditions
# -------------------------------------------
# Three practice problems similar to the shop‑discount question.

# Q1. Movie Ticket Pricing
# ------------------------
# If age is above 60, check if they have a senior citizen card.
#   - If yes → 50% discount
#   - If no → 30% discount
# Else if age is between 18 and 60 → no discount
# Else (below 18): provide 20% student discount.

age= int(input("enter the age of customer: "))
if age>=60:
    print("50% discount")
elif age <60 and age >18:
    print("no discount")

else:
    print("20% discount")




# Q2. Exam Eligibility Checker
# ----------------------------
# If attendance is above 75%, check if assignment submission is complete.
#   - If complete → print "Eligible for exam"
#   - Else → print "Submit assignments first"
# If attendance is below 75% → print "Not enough attendance"


# Q3. Internet Package Selection
# ------------------------------
# If user chooses "premium" plan, check if they want annual billing.
#   - If yes → give 25% discount
#   - If no → no discount
# If user chooses "basic" plan → check if data usage is below 100GB
#   - If below 100GB → give 5% discount
#   - Else → no discount
