import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#==============================Reading CSV Files=========================================
def read():
            cod=input('Enter the Code of State or Press I for Data of whole India:')
            if cod=='a1':
                        df=pd.read_csv('F:\OFFICIAL PROJECTS\Data Analysis System\csv files\\andaman nicobar.csv'  ,  nrows=153)
            if cod=='a2':
                        df=pd.read_csv('F:\OFFICIAL PROJECTS\Data Analysis System\csv files\\andhra pradesh.csv'  ,  nrows=153)
            if cod=='a3':
                        df=pd.read_csv('F:\OFFICIAL PROJECTS\Data Analysis System\csv files\\arunachal pradesh.csv'  ,  nrows=153)
            if cod=='a4':
                        df=pd.read_csv('F:\OFFICIAL PROJECTS\Data Analysis System\csv files\\assam.csv'  ,  nrows=153 )
            if cod=='a5':
                        df=pd.read_csv('F:\OFFICIAL PROJECTS\Data Analysis System\csv files\\bihar.csv'  ,  nrows=153)
            if cod=='a6':
                        df=pd.read_csv('F:\OFFICIAL PROJECTS\Data Analysis System\csv files\\chandigarh.csv'  ,  nrows=153)
            if cod=='a7':
                        df=pd.read_csv('F:\OFFICIAL PROJECTS\Data Analysis System\csv files\\chhatisgarh.csv'  ,  nrows=153)
            if cod=='a8':
                        df=pd.read_csv('F:\OFFICIAL PROJECTS\Data Analysis System\csv files\\dadar and nagar haveli.csv'  ,  nrows=153)
            if cod=='a9':
                        df=pd.read_csv('F:\OFFICIAL PROJECTS\Data Analysis System\csv files\\delhi.csv'  ,  nrows=153)
            if cod=='a10':
                        df=pd.read_csv('F:\OFFICIAL PROJECTS\Data Analysis System\csv files\\goa.csv'  ,  nrows=153)
            if cod=='b1':
                        df=pd.read_csv('F:\OFFICIAL PROJECTS\Data Analysis System\csv files\\gujrat.csv'  ,  nrows=153)
            if cod=='b2':
                        df=pd.read_csv('F:\OFFICIAL PROJECTS\Data Analysis System\csv files\\haryana.csv'  ,  nrows=153)
            if cod=='b3':
                        df=pd.read_csv('F:\OFFICIAL PROJECTS\Data Analysis System\csv files\\himachal pradesh.csv'  ,  nrows=153)
            if cod=='b4':
                        df=pd.read_csv('F:\OFFICIAL PROJECTS\Data Analysis System\csv files\\jammukashmir.csv'  ,  nrows=153)
            if cod=='b5':
                        df=pd.read_csv('F:\OFFICIAL PROJECTS\Data Analysis System\csv files\\jharkhand.csv'  ,  nrows=153)
            if cod=='b6':
                        df=pd.read_csv('F:\OFFICIAL PROJECTS\Data Analysis System\csv files\\karnataka.csv'  ,  nrows=153)
            if cod=='b7':
                        df=pd.read_csv('F:\OFFICIAL PROJECTS\Data Analysis System\csv files\\kerala.csv'  ,  nrows=153)
            if cod=='b8':
                        df=pd.read_csv('F:\OFFICIAL PROJECTS\Data Analysis System\csv files\\ladakh.csv'  ,  nrows=153)
            if cod=='b9':
                        df=pd.read_csv('F:\OFFICIAL PROJECTS\Data Analysis System\csv files\\madhyapradesh.csv'  ,  nrows=153)
            if cod=='b10':
                        df=pd.read_csv('F:\OFFICIAL PROJECTS\Data Analysis System\csv files\\maharashtra.csv'  ,  nrows=153)
            if cod=='c1':
                        df=pd.read_csv('F:\OFFICIAL PROJECTS\Data Analysis System\csv files\\manipur.csv'  ,  nrows=153)
            if cod=='c2':
                        df=pd.read_csv('F:\OFFICIAL PROJECTS\Data Analysis System\csv files\\meghalaya.csv'  ,  nrows=153)
            if cod=='c3':
                        df=pd.read_csv('F:\OFFICIAL PROJECTS\Data Analysis System\csv files\\mizoram.csv'  ,  nrows=153)
            if cod=='c4':
                        df=pd.read_csv('F:\OFFICIAL PROJECTS\Data Analysis System\csv files\\nagaland.csv'  ,  nrows=153)
            if cod=='c5':
                        df=pd.read_csv('F:\OFFICIAL PROJECTS\Data Analysis System\csv files\\odisha.csv'  ,  nrows=153)
            if cod=='c6':
                        df=pd.read_csv('F:\OFFICIAL PROJECTS\Data Analysis System\csv files\\puducherry.csv'  ,  nrows=153)
            if cod=='c7':
                        df=pd.read_csv('F:\OFFICIAL PROJECTS\Data Analysis System\csv files\\punjab.csv'  ,  nrows=153)
            if cod=='c8':
                        df=pd.read_csv('F:\OFFICIAL PROJECTS\Data Analysis System\csv files\\rajasthan.csv'  ,  nrows=153)
            if cod=='c9':
                        df=pd.read_csv('F:\OFFICIAL PROJECTS\Data Analysis System\csv files\\sikkim.csv'  ,  nrows=153)
            if cod=='c10':
                        df=pd.read_csv('F:\OFFICIAL PROJECTS\Data Analysis System\csv files\\tamilnadu.csv'  ,  nrows=153)
            if cod=='d1':
                        df=pd.read_csv('F:\OFFICIAL PROJECTS\Data Analysis System\csv files\\telengana.csv'  ,  nrows=153)
            if cod=='d2':
                        df=pd.read_csv('F:\OFFICIAL PROJECTS\Data Analysis System\csv files\\tripura.csv'  ,  nrows=153)
            if cod=='d3':
                        df=pd.read_csv('F:\OFFICIAL PROJECTS\Data Analysis System\csv files\\uttarakhand.csv'  ,  nrows=153)
            if cod=='d4':
                        df=pd.read_csv('F:\OFFICIAL PROJECTS\Data Analysis System\csv files\\uttarpradesh.csv'  ,  nrows=153)
            if cod=='d5':
                        df=pd.read_csv('F:\OFFICIAL PROJECTS\Data Analysis System\csv files\\westbengal.csv'  ,  nrows=153)
            if cod=='I' or cod=='i':
                        df=pd.read_csv('F:\OFFICIAL PROJECTS\Data Analysis System\csv files\\India.csv'  ,  nrows=153)
            global data
            data=df
            return data
           
#================================ List of states and union territories==================================
list1=['a1 :Andaman and Nicobar' , 'a2: Andhra Pradesh' , 'a3: Arunachal Pradesh' , 'a4: Assam' , 'a5: Bihar']
list2=['a6: Chandigarh' , 'a7: Chhatisgarh' , 'a8: Dadar and Nagar Haveli' , 'a9: Delhi ' , 'a10: Goa']
list3=['b1: Gujarat' , 'b2: Haryana' , 'b3: Himachal Pradesh' , 'b4: Jammu and Kashmir ' , 'b5: Jharkhand']
list4=['b6: Karnataka' , 'b7: Kerala' , 'b8: Ladakh' , 'b9: Madhya Pradesh ' , 'b10: Maharashtra']
list5=['c1: Manipur ' , 'c2: Meghalaya' , 'c3: Mizoram' , 'c4: Nagaland ' , 'c5: Odisha']
list6=['c6: Puducherry' , 'c7: Punjab' , 'c8: Rajasthan' , 'c9: Sikkim ' , 'c10: Tamil Nadu']
list7=['d1: Telengana' , 'd2: Tripura' , 'd3: Uttarakhand' , 'd4: Uttar Pradesh ' , 'd5: West Bengal']
#===========================================================================================

#1. Data Manipulation Function
def manipulation():
            ys='y'
            while ys=='y':
                        read()
                        df=pd.DataFrame(data)
                        print('************************************************')
                        print('*      Select the Operation                    *')
                        print('************************************************')
                        print('*1. Showing Data                               *')
                        print('*2. Delete Records                             *')
                        print('*3. Adding New Data                            *')
                        print('*4. Return to Main Menu                        *')
                        print('************************************************')
                        inp=int(input('Enter Your Choice'))
                        if inp==1:
                                    print(df)
                        if inp==2:
                                    print('1.Delete only one record:')
                                    print('2.Delete two records:')
                                    print('3.Delete range of  records:')
                                    n=int(input('Enter Your choice'))
                                    print(df)
                                    if n==1:
                                                a=input('Enter the index number:')
                                                print(df.drop(a))
                                    if n==2:
                                                c , b=input('Enter the index numbers with coomas:')
                                                print(df.drop([c , d]))
                                    if n==3:
                                                a=int(input('Enter first element of range:'))
                                                d=int(input('Enter Last element of range:'))
                                                print(df.drop(df.index[a:d]))
                                    else:
                                                print('Invalid Choice')
                        if inp==3:
                                    print(df)
                                    l1=[]
                                    l2=[]
                                    l3=[]
                                    re=int(input('Enter Number of records'))
                                    for x in range(0 , re):
                                                a=input('Enter the Date {dd-mm-yy}:')
                                                b=input('Enter number of Cases:')
                                                c=input('Enter Deaths')
                                                l1.append(a)
                                                l2.append(b)
                                                l3.append(c)
                                    dic={'Date':l1 , 'Cases':l2 , 'Deaths':l3}
                                    df1=pd.DataFrame(dic)
                                    df=pd.concat([df , df1] ,  ignore_index=True)
                                    print(df)
                                    print('New Data added successfully')
                                    
                        if inp==4:
                                    break
                        
#2. Data Visualisation Function
def visualise():
            ans='n'
            while ans=='n' or ans=='N':
                        read()
                        df=pd.DataFrame(data)
                        mon=['April' , 'May' , 'June' , 'July' , 'August']
                        cvals=list(df['Cases'])
                        dvals=list(df['Deaths'])
                        ap1=cvals[0:30]
                        ma1=cvals[30:61]
                        j1=cvals[61:92]
                        jy1=cvals[92:124]
                        ag1=cvals[124:]
                        ap2=dvals[0:30]
                        ma2=dvals[30:61]
                        j2=dvals[61:92]
                        jy2=dvals[92:124]
                        ag2=dvals[124:]

                        sum1=[sum(ap1)/len(ap1) , sum(ma1)/len(ma1) , sum(j1)/len(j1) , sum(jy1)/len(jy1) , sum(ag1)/len(ag1)]
                        sum2=[sum(ap2)/len(ap2) , sum(ma2)/len(ma2) , sum(j2)/len(j2) , sum(jy2)/len(jy2) , sum(ag2)/len(ag2)]

                        print('*************************************')
                        print('*              Charts               *')
                        print('*************************************')
                        print('* 1.Line Chart                      *')
                        print('* 2.Bar Chart                       *')
                        print('* 3.Scatter Chart                   *')
                        print('* 4.Pie Chart                       *')
                        print('* 5.Box Plot                        *')
                        print('* 6.Exit                            *')
                        print('*************************************')
                        cis=int(input('Enter Number of Chart:'))
                        if cis==1:
                                    plt.plot(mon , sum1 , label='Cases' , color='b')
                                    plt.plot(mon , sum2 , label='Deaths' ,  color='r')
                                    plt.xlabel('Months' ,  fontsize=14 ,  color='k')
                                    plt.ylabel('Avg no. of Cases/Deaths' ,  fontsize=14 ,  color='k')
                                    plt.title('Covid Cases and Deaths from April to August',fontsize=18)
                                    plt.legend()
                                    plt.show()
                        if cis==2:
                                    x=np.arange(1 , 6)
                                    plt.xticks(x ,  mon)
                                    plt.bar(x , sum1 , width=0.25 , label='Cases' , color='b')
                                    plt.bar(x+0.25 , sum2 , width=0.25 , label='Deaths' ,  color='r')
                                    plt.xlabel('Months' ,  fontsize=14 ,  color='k')
                                    plt.ylabel('Avg no. of Cases/Deaths' ,  fontsize=14 ,  color='k')
                                    plt.title('Covid Cases and Deaths from April to August',fontsize=18)
                                    plt.legend()
                                    plt.show()
                        if cis==3:
                                    plt.scatter(mon , sum1 , label='Cases' , color='b')
                                    plt.scatter(mon , sum2 , label='Deaths' ,  color='r')
                                    plt.xlabel('Months' ,  fontsize=14 ,  color='k')
                                    plt.ylabel('Avg no. of Cases/Deaths' ,  fontsize=14 ,  color='k')
                                    plt.title('Covid Cases and Deaths from April to August',fontsize=18)
                                    plt.legend()
                                    plt.show()
                        if cis==4:
                                    av=input('Press d for Death Pie Chart or Press c for Cases Pie C ')
                                    if av=='c':
                                                plt.pie(sum1 , labels=mon , colors=['b' , 'r' , 'y' , 'g' , 'c'] , shadow=True ,  autopct='%0.1f%%')
                                                plt.title('Average Cases Per Month' ,  fontsize=16)
                                                plt.title('Covid Cases from April to August',fontsize=18)
                                                plt.legend(loc="upper left")
                                                plt.show()
                                                            
                                    if av=='d':
                                                plt.pie(sum2 , labels=mon , colors=['b' , 'r' , 'y' , 'g' , 'c'] , shadow=True ,  autopct='%0.1f%%')
                                                plt.title('Average Deaths Per Month' ,  fontsize=16)
                                                plt.title('Covid Deaths from April to August',fontsize=18)
                                                plt.legend(loc="upper right")
                                                plt.show()
                        if cis==5:
                                    lab=['Cases' , 'Deaths']
                                    boxdata=[sum1 , sum2]
                                    plt.boxplot(boxdata , vert=1 ,  patch_artist=True ,  labels=lab)
                                    plt.show()
                        if cis==6:
                                    break

#3. Mathematical operations Function
def operations():
            ad='y'
            while ad=='y':
                        read()
                        df=pd.DataFrame(data)
                        print('************************************************')
                        print('*          Select the Operation                *')
                        print('************************************************')
                        print('* 1.To Calculate Maximum                       *')
                        print('* 2.To Calculate Minimum                       *')
                        print('* 3.To Calculate Sum                           *')
                        print('* 4.To Calculate Mean                          *')
                        print('* 5.To Calculate Median                        *')
                        print('* 6.To Calculate Satandard deviation           *')
                        print('* 7.To Calculate Variance                      *')
                        print('* 8.To Calculate Quantiles                     *')
                        print('* 9.Exit                                       *')
                        print('************************************************')
                        gh=int(input('Enter the number of Operation(without decimal):'))
                        if gh==1:
                                    print('Maximum Cases and Deaths')
                                    print(df.max())
                                    ad=input('Press y to return to operation menu or Press n to exit')
                        if gh==2:
                                    print('Minimum Cases and Deaths')
                                    print(df.min())
                                    ad=input('Press y to return to operation menu or Press n to exit')
                        if gh==3:
                                    print('Total Cases')
                                    print(df['Cases'].sum(skipna=True))
                                    print('Total Deaths')
                                    print(df['Deaths'].sum(skipna=True))
                                    ad=input('Press y to return to operation menu or Press n to exit')
                        if gh==4:
                                    print('Mean of Data')
                                    print(df.mean(skipna=True).round(2))
                                    ad=input('Press y to return to operation menu or Press n to exit')
                        if gh==5:
                                    print('Median of Data')
                                    print(df.median(skipna=True).round(2))
                                    ad=input('Press y to return to operation menu or Press n to exit')
                        if gh==6:
                                    print('Standard deviation of data')
                                    print(df.std(skipna=True).round(2))
                                    ad=input('Press y to return to operation menu or Press n to exit')
                        if gh==7:
                                    print('Variance of data')
                                    print(df.var(skipna=True))
                                    ad=input('Press y to return to operation menu or Press n to exit')
                        if gh==8:
                                    print('First Quantile')
                                    print(df.quantile(0.25))
                                    print('Second Quantile')
                                    print(df.quantile(0.50))
                                    print('Third Quantile')
                                    print(df.quantile(0.75))
                                    ad=input('Press y to return to operation menu or Press n to exit')
                        if gh==9:
                                    break

#4. More Operations Function
def Moperations():
            s='y'
            while s=='y':
                        read()
                        df=pd.DataFrame(data)
                        print('*****************************************')
                        print('*          Select the Operation         *')
                        print('*****************************************')
                        print('* 1.Pivoting                            *')
                        print('* 2.Sorting                             *')
                        print('* 3.To see 7 statistical values of data *')
                        print('* 4.Rename the Column                   *')
                        print('* 5.Transpose the Data                  *')
                        print('* 6.Return to Main Menu                 *')
                        print('*****************************************')
                        ch=int(input('Enter the number of operation:'))
                        if ch==1:
                                    print(df)
                                    print('Select the attributes')
                                    print('Date ,  Cases ,  Deaths')
                                    a=str(input('Enter name for Column:'))
                                    b=str(input('Enter name for Index'))
                                    c=str(input('Enter name for values'))
                                    print(df.pivot(index=b , columns=a , values=c))
                        if ch==2:
                                    print('Select the Column for sorting : [Cases ,  Deaths]')
                                    g=input('Press C for Cases or Press D for Deaths:')
                                    if g=='c' or g=='C':
                                                v=input('Press A for ascending or D for Descending:')
                                                if v=='A' or v=='a':
                                                            print(df.sort_values('Cases'))
                                                else:
                                                            print(df.sort_values('Cases' ,  ascending=False))
                                    if g=='d' or g=='D':
                                                u=input('Press A for ascending or D for Descending:')
                                                if u=='A' or u=='a':
                                                            print(df.sort_values('Deaths'))
                                                else:
                                                            print(df.sort_values('Deaths' ,  ascending=False))
                        if ch==3:
                                    print(df.describe())
                        if ch==4:
                                    a=str(input('Enter the old column name:'))
                                    b=str(input('Enter the new column name:'))
                                    c=input('Press P for Permanent change or Press T for Temporary Change:')
                                    if c=='p' or c=='P':
                                                print(df.rename(columns={a:b} ,  inplace=True))
                                    if c=='t' or c=='T':
                                                print(df.rename(columns={a:b}))
                        if ch==5:
                                    print(df.T)
                        if ch==6:
                                    break

#5. Mysql connectivity
def conn():
            ab='y'
            while ab=='y':
                        a=mysql.connector.connect(host="localhost" ,  user="root" ,  passwd= "123456" , database="covid_data")
                        print('########################## LIST OF TABLES #########################################')
                        print('andaman_nicobar , andhra_pradesh  , arunachal_pradesh , assam , bihar , chandigarh')             
                        print('chhatisgarh , dadar_and_nagar_haveli  , delhi , goa , gujarat , haryana , himachalpradesh')
                        print('india , jammukashmir , jharkhand , karnataka , kerala , ladakh , madhyapradesh , maharashtra')            
                        print('manipur , meghalaya , mizoram , nagaland , odisha , puducherry , punjab , rajasthan , sikkim')                 
                        print('tamilnadu , telengana , tripura , uttarakhand , uttarpradesh , westbengal')
                        print('####################################################################################')
                        cur=a.cursor(buffered=True)
                        qr=str(input('Enter Your Query'))
                        cur.execute(qr)
                        myrecords=cur.fetchall()
                        for x in myrecords:
                                    print(x)
                        ab=input('Press y to continue or Press n to return to Main Menu')

#6. Codes for States
def codes():
            print('#################################################################################################')
            print('                       Codes for States / Union Territories                                                                   ')
            print(list1)
            print(list2)
            print(list3)
            print(list4)
            print(list5)
            print(list6)
            print(list7)
            print('#################################################################################################')


                                    
# Main Menu Function
av='y'
while av=='y':
            print('==========================================')
            print(' Covid-19 Data Analysis System for India          ')
            print('==========================================')
            print('1. Data Manipulation              ')
            print('2. Data Visualisation                                                     ')
            print('3. Mathematical Operations on data                           ')
            print('4. Some More Operations                                             ')
            print('5. Exit the Program                                                       ')
            print('==========================================')
            choice=int(input('Enter your choice:'))
                        
            if choice==1:
                          codes()
                          manipulation()
            if choice==2:
                          codes()
                          visualise()
            if choice==3:
                          codes()
                          operations()
            if choice==4:
                          codes()
                          Moperations()
            if choice==5:
                          quit()
                        
