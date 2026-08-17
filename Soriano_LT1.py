# We use amount_notebooks for the total of notebooks and we ask the user on how many notebooks we are going to deliver.
amount_notebooks = int(input("Enter the amount of notebooks: "))

# We use box_capacity for the total of boxes out in delivery and its capacity
box_capacity = int(input("Enter storage capacity of boxes: "))

# total_boxes will be our equation if there is no excess notebook/s
total_boxes = amount_notebooks // box_capacity

# excess will be our equation if there are excess notebooks and they will be put in a loose pack.
excess = amount_notebooks % box_capacity

# This is the final output of the program, it shows us on what will happen if we add the users given info and how many notebooks are in a box and how many are put in a loose pack.
if excess == 0:
    print(f"There will be {total_boxes} boxes")
else:
      print(f"There will be {total_boxes} full boxes and {excess} will go to a loose pack.")