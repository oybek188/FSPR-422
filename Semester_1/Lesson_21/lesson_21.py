name = "Oybek"

"""
Merge conflict

Вам нужно создать ветку из главной ветки 
Потом в главной ветке создаете изменения, фиксируете и публикуете: git add, git commit, git push 
 
Потом переходите на вашу созданную ветку в которой вы ведете разработку  
(меняете одну и ту же строчку кода как и в main) фиксируете и публикуете:  
git add, git commit, git push 
и создаёте pull request чтобы связать изменения с главной веткой и у вас должен произойти  
merge conflict 
 
Способ его решения: 
git rebase main (название ветки) 
 
hint: Resolve all conflicts manually, mark them as resolved with 
hint: "git add/rm <conflicted_files>", then run "git rebase --continue" 
 
Решаете конфликт от руки и добавляете изменения с помощью команды git add/rm 
потом пишите git rebase --continue 
потом открывается окно коммита, в котором можно менять сообщение коммита или оставить и закрыть файл 
потом написать в консоли 
git push -f

"""