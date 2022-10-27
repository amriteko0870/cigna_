import pandas as pd
def output(df):
    data_1 = df
    output = pd.pivot_table(data=data_1,index=['ULTIMATE_DUNS_NUMBER'],values=['New_Customer_Match'],columns=['Control'],aggfunc={'New_Customer_Match':'sum','Control':'count'})

    output_1 = output.reset_index()


    output_1['#_of_Test'] =output_1['Control'][0]
    output_1['#_of_Control'] = output_1['Control'][1]


    output_1['#_of_prospect_Test'] = output_1['New_Customer_Match'][0]
    output_1['#_of_prospect_Control'] = output_1['New_Customer_Match'][1]

    output_1.drop(columns=['Control','New_Customer_Match'],axis=1,inplace=True)

    output_1['Value_counts_ultimate_duns_num'] = output_1['#_of_Test'] + output_1['#_of_Control']

    output_1['Total_sum_of_new_coustmer_match'] = output_1['#_of_prospect_Test'] + output_1['#_of_prospect_Control']

    output_1['Conversion_rate_test'] = round((output_1['#_of_prospect_Test']/output_1['#_of_Test'])*100,2)

    output_1['Conversion_rate_control'] = round((output_1['#_of_prospect_Control']/output_1['#_of_Control'])*100,2)

    # output_1['Lift'] = round(output_1['Conversion_rate_control']/output_1['Conversion_rate_test'],2)
    l = []
    for i in range(output_1.shape[0]):
        try:
            a = round(list(output_1['Conversion_rate_control'])[i]/list(output_1['Conversion_rate_test'])[i],2)
        except:
            a = 0
        l.append(a)
    output_1['Lift'] = l
    return output_1

def output2(df,name):
    data_1 = df
    output_2_1 = pd.pivot_table(data=data_1,index=[name],values=['New_Customer_Match'],columns=['Control'],aggfunc={'New_Customer_Match':'sum','Control':'count'})

    output_2 = output_2_1.reset_index()


    output_2['#_of_Test'] =output_2['Control'][0]
    output_2['#_of_Control'] = output_2['Control'][1]


    output_2['#_of_prospect_Test'] = output_2['New_Customer_Match'][0]
    output_2['#_of_prospect_Control'] = output_2['New_Customer_Match'][1]

    output_2.drop(columns=['Control','New_Customer_Match'],axis=1,inplace=True)

    output_2['Value_counts'] = output_2['#_of_Test'] + output_2['#_of_Control']

    output_2['Total_sum_of_new_coustmer_match'] = output_2['#_of_prospect_Test'] + output_2['#_of_prospect_Control']

    output_2['Conversion_rate_test'] = round((output_2['#_of_prospect_Test']/output_2['#_of_Test'])*100,2)

    output_2['Conversion_rate_control'] = round((output_2['#_of_prospect_Control']/output_2['#_of_Control'])*100,2)

    # output_1['Lift'] = round(output_1['Conversion_rate_control']/output_1['Conversion_rate_test'],2)
    l = []
    for i in range(output_2.shape[0]):
        try:
            a = round(list(output_2['Conversion_rate_control'])[i]/list(output_2['Conversion_rate_test'])[i],2)
        except:
            a = 0
        l.append(a)
    output_2['Lift'] = l

    output_2['probability_Test_0'] =  1- data_1['Choice1A_p_1']
    output_2['probability_Test_1'] = data_1['Choice1A_p_1']

    output_2['Overall_conversion_rate'] = output_2['Total_sum_of_new_coustmer_match']/output_2['Value_counts']

    output_2['Test'] = output_2['#_of_prospect_Test']/output_2['#_of_Test']

    output_2['Control'] = output_2['#_of_prospect_Control']/output_2['#_of_Control']

    output_2['Cumm_conversion'] = output_2['Overall_conversion_rate'].cumsum()

    output_2['Cumm_Test'] = output_2['Test'].cumsum()

    output_2['Cumm_Control'] = output_2['Control'].cumsum()

    return output_2

