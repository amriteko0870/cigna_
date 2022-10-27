import os
from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from dataApp.extra import output2

from dataApp.models import cigna_data

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def index(request,format=None):
    data = pd.read_csv("cigna.csv")
    out = output2(data,'Choice1A_Decile')
    out.fillna(0,inplace=True)
    out1 = output2(data,'Choice1C_Decile')
    out1.fillna(0,inplace=True)
    n = out.to_dict(orient='records')
    m = out1.to_dict(orient='records')
    # sheet_cols = ['Choice1A_Decile',
    #                 'no_of_Test',
    #                 'no_of_Control',
    #                 'no_of_prospect_Test',
    #                 'no_of_prospect_Control',
    #                 'Value_counts',
    #                 'Total_sum_of_new_coustmer_match',
    #                 'Conversion_rate_test',
    #                 'Conversion_rate_control',
    #                 'Lift']
    # graph_cols = ['Choice1A_Decile',
    #                 'probability_Test_1',
    #                 'probability_Test_0',
    #                 'Overall_conversion_rate',
    #                 'Test',
    #                 'Control',
    #                 'Cumm_conversion',
    #                 'Cumm_Test',
    #                 'Cumm_Control']
    df = pd.DataFrame(n)
    ndf = pd.DataFrame(m)
    
    for i in df.columns:
        x = i[0].replace("#", "no")
        df = df.rename(columns={i: x})
    
    for i in ndf.columns:
        if i[0] == 'Choice1C_Decile':
            print('#######################################hello')
            ndf = ndf.rename(columns={i: 'Choice1A_Decile'})
        else:
            x = i[0].replace("#", "no")
            ndf = ndf.rename(columns={i: x})
        print(x)
        

    # sheet_data = df[sheet_cols].to_dict(orient='records')
    # graph_data = df[graph_cols].to_dict(orient='records')
    sheet_data1 = df.to_dict(orient='records')
    graph_data1 = df.to_dict(orient='records')
    sheet_data2 = ndf.to_dict(orient='records')
    graph_data2 = ndf.to_dict(orient='records')
    return Response({'status':'successful',
                        'data':[{
                        'header_name':'Choice 1A',
                         'data':sheet_data1,
                         'graph':graph_data1
                                },
                                {
                        'header_name':'Choice 1C',
                         'data':sheet_data2,
                         'graph':graph_data2
                                },
                               ]
                                }) 



