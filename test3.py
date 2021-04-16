# Student(S#,Sname,Sage,Ssex)学生表
# S#：学号
# Sname：学生姓名
# Sage：学生年龄
# Ssex：学生性别

# Course(C#,Cname,T#)课程表
# C#：课程编号
# Cname：课程名称
# T#：教师编号

# SC(S#,C#,score)成绩表
# S#：学号
# C#：课程编号
# score：成绩


# Teacher(T#,Tname)教师表
# T#：教师编号：
# Tname：教师名字


'''
1、查询“001”课程比“002”课程成绩高的所有学生的学号
select a.s# from (select s#,score from SC where c#='001')a,(se where c#='002')b where a.s#=b.s# and a.score>b.score;


2、查询平均成绩大于60分的同学的学号和平均成绩
select s#,avg(score) form sc group by s# having avg(score)>60;

3、查询所有同学的学号、姓名、选课数、总成绩
select student.s#,student.sname,count(sc.c#),sum(sc.score)from student
left join sc on student.s#=sc.c#
group by student.s#,student.sname;

4、查询姓‘李’的老师的个数：
select count(distinct(Tname)) from Teacher where Tname like '李%'；

5、查询没有学过“叶平”老师课程的同学的学号、姓名：
select student student.s#,student.sname from student where
s# not in (select sc.s# from sc,course,teacher where sc.c#=course.c# and
course.T#=teacher.T# and Teacher.Tname='叶平')


6/查询学过叶平老师课程的同学的学号、姓名
select student.s#,student.sname from student where s# in (select sc.s# from
sc,course,teacher where where sc.c#=course.c# and
course.T#=teacher.T# and Teacher.Tname='叶平'
group by s#
having count(sc.c#)=(select count(c#)from course,teacher where
teacher.T#=course.T# and Tname='叶平'))；



7、查询学过“011”并且也学过编号“002”课程的同学的学号、姓名：
select student.s#,sname from student,sc where
student.s#=sc.s# and c#='001' and
exisit (select * from sc as sc_2 where sc.s#=sc_2.s# and sc_2.s#='002')


8、查询课程编号“002”的成绩比课程编号“001”课程低的所有同学的学号、姓名：
Select S#,Sname
from (select Student.S#,Student.Sname,score ,
(select score from SC SC_2 where SC_2.S#=Student.S# and SC_2.C#='002') score2
from Student,SC
where Student.S#=SC.S# and C#='001') S_2
where score2 < score;






'''

