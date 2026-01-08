'''Input Format

The first line contains an integer, , the number of students.
The  subsequent lines describe each student over  lines.
- The first line contains a student's name.
- The second line contains their grade.

Constraints

There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

Sample Input 0

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Sample Output 0

Berry
Harry'''
#code
'''n = int(input())

students = []
scores = []

for _ in range(n):
    name = input()
    score = float(input())
    
    students.append([name, score])
    scores.append(score)

lowest = min(scores)
second_lowest = min(s for s in scores if s != lowest)

result = [name for name, score in students if score == second_lowest]
result.sort()

for name in result:
    print(name)
'''