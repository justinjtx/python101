# ask the user for a height and print a pryamid that is that many rows tall

# height = 5
# width =  1

# for i in range(0, height):
#     row = ("")
#     width = "\t", width + 2
#     for j in range(0, width):
#         row = row + "*"
#     print(row)


height = 5
base = height * 2
for row in range(height):
    string_row = ""
    for star in range(base):
        if star < height - row or star > height + row and star != height:
            string_row += " "
        else:
            string_row += "*"
    print(string_row)

    