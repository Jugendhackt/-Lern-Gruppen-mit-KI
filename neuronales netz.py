person1[] = {"Gymnasium","17-18","Deutsch", "durch Lesen", "Sport orientiert", "Ich bin organisiert", "Ich kann nicht gut zuhören"}
person2[] = {""}

person1[0] = "Grundschule"
person2[0] = "Grundschule" 
end_score = 0

for i in range(person1):
    if person1[i] == person2[i]:
        end_score += 1

print("Endscore: " + str(end_score))