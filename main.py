import numpy as np
import data_loader

id , name , data  = data_loader.all_data()
id = data_loader.array_converter(id)
name = data_loader.array_converter(name)
data = data_loader.array_converter(data)
# Total student 
total_student = len(id)

# Average marks in each subject
average_python = np.mean(data[:,0])
average_csa = np.mean(data[:,1])
average_mc = np.mean(data[:,2])

# Attendance and Study hour
average_attendance = np.mean(data[:,3])
average_study_hour = np.mean(data[:,4])

# Student below 75% attendance  
below_75 = name[data[:,3]<75]
low_attendance = '\n    '.join(f"{index}. {naam}" for index,naam in enumerate(below_75,start=1))


# Student who Studies more than 4 hr 
more_4hr = name[data[:,4]>4]
high_study = '\n    '.join(f'{index}. {naam}'for index ,naam in enumerate(more_4hr,start=1))

# Student-wise Averages 
average_student = list(map(np.mean,data[:,:3]))
student_average = '\n    '.join(f'{index+1}. {name[index]}  -  {average:.2f}%' for index , average in enumerate(average_student))

# Top performer 
Top_student = name[np.argmax(average_student)]
Low_student = name[np.argmin(average_student)]