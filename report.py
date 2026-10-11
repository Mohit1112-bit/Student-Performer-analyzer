import main,helper
with open('analysis.txt','w') as f :
    f.write("="*51)
    f.write('STUDENT PERFORMANCE ANALYSIS'.center(51))
    f.write("="*51)
    f.write(f'''


    Total Student :  {main.total_student}
    

    


    Average Marks 
    {helper.sep()}
   {'Python':<10}  :  {main.average_python:.2f}
   {'CSA':<10}  :  {main.average_csa:.2f}
   {'MC':<10}  :  {main.average_mc:.2f}
      




    Average Attendance 
    {helper.sep()}
    {'Average Attendance':<10}  :  {main.average_attendance}%
    {'Average Study hour':<10}  :  {main.average_study_hour}
    



    Student less than 75 Attendance 
    {helper.sep()}
    {main.low_attendance}




    Student Who studies more than 4hr
    {helper.sep()}
    {main.high_study}




    Student-wise Average 
    {helper.sep()}
    {main.student_average}



    Top & Lowest Performer 
    {helper.sep()}
    {f'Top Performer            Lowest Performer':<20} 
    {main.Top_student}                     {main.Low_student}

    ''')