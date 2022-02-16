#dict={"name": "Plato", "country": "Ancient Greece", "born": -427, "teacher": "Socrates", "student": "Aristotle"}
#  Verilen dictionary-e esasen asgidaki suallari cavablandirmaq ucun ekrana sualin cavabiniz yazdirin. 
# Bunun ucun userden input alin. Eger user “born”, “when” sozlerini daxil etse program texmin etsin ki user 
# ne sorushmaq isteyir. Meselen born ve when sozleri varsa cumlede user cox guman ki “When was Plato born?” 
# sualina cavab axtarir. Proqram o sozleri gorub sorushsun ki, “Maybe did you mean “When was Plato born?” “.
#  Bu suali sorushduqda yes ve no secimleri verin. Eger yes yazsa dictionarydeki datadan istifade ederek
#  Platonun doguldugu ili usere gosterin.Meselen country daxil etse proqram texmin etsin ki user platonun 
# doguldugu yeri axtarir ve siz de ele proqram yazin ki ona uygun cavab qaytarin. 
# Eger mentiqsiz soz daxil edilse not found verin ekrana.
dict={"name": "Plato", "country": "Ancient Greece", "born": -427, "teacher": "Socrates", "student": "Aristotle"}
word = input('writing thing:')
def sual_cavab(x):
    for i in x:
        if word =='born' or word =='when':
            print('Maybe did you mean “When was Plato born?')
            yes_no =input('answer:')
            if yes_no =='yes':
             answer= dict.get('born')
             return answer
            else:
             break
        if word == 'country' or word == 'where':
              print('Maybe did you mean “Where was Plato born?')
              yes_no =input('answer:')
              if yes_no =='yes':
                   answer= dict.get('country')
                   return answer
              else:
                  break
        if word == 'name' or word == 'who':
              print('Maybe did you mean “What is his name?')
              yes_no =input('answer:')
              if yes_no =='yes':
                   answer= dict.get('name')
                   return answer
              else:
                  break
        if word == 'teacher' or word == 'subject':
              print('Maybe did you mean "Which is subject teacher?"')
              yes_no =input('answer:')
              if yes_no =='yes':
                   answer= dict.get('teacher')
                   return answer
              else:
                  break
        if word == 'student':
              print('Maybe did you mean "Who is student?"')
              yes_no =input('answer:')
              if yes_no =='yes':
                   answer= dict.get('teacher')
                   return answer
              else:
                  break  
    if word not in dict:
         return 'Not found'
print(sual_cavab(dict))       