import json
import plotly
import plotly.express as px
from models.hsol import caller as cl1
from models.fakeddit_2 import caller as cl2
from models.fakeddit_6 import caller as cl3
from models.implicit_3 import caller as cl4
from models.implicit_6 import caller as cl5
import logging

def user_plots(df, app):
    #hsol
    data_1=cl1(df)
    get_0_data_1=data_1.loc[data_1['Category']==0]
    sorted_1_0=get_0_data_1.groupby("User").size()
    sorted_1_0=sorted_1_0.sort_values(ascending=False)
    sorted_1_0=sorted_1_0[0:5]
    fig = px.bar(x=sorted_1_0.index, y=sorted_1_0)
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="Number of tweets")
    fig.update_layout(showlegend=False)
  
    fig.update_layout(xaxis={'showticklabels': False})    
    graphJSON_1_0 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    get_1_data_1=data_1.loc[data_1['Category']==1]
    sorted_1_1=get_1_data_1.groupby("User").size()
    sorted_1_1=sorted_1_1.sort_values(ascending=False)
    sorted_1_1=sorted_1_1[0:5]
    fig = px.bar(x=sorted_1_1.index, y=sorted_1_1)
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="Number of tweets")
    fig.update_layout(showlegend=False)
   
    fig.update_layout(xaxis={'showticklabels': False})    
    graphJSON_1_1 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    get_2_data_1=data_1.loc[data_1['Category']==2]
    sorted_1_2=get_2_data_1.groupby("User").size()
    sorted_1_2=sorted_1_2.sort_values(ascending=False)
    sorted_1_2=sorted_1_2[0:5]
    fig = px.bar(x=sorted_1_2.index, y=sorted_1_2)
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="Number of tweets")
    fig.update_layout(showlegend=False)
   
    fig.update_layout(xaxis={'showticklabels': False})    
    graphJSON_1_2 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    graphJSON_1_ = []
    
    graphJSON_1_.append(graphJSON_1_0)
    graphJSON_1_.append(graphJSON_1_1)
    graphJSON_1_.append(graphJSON_1_2)
    #fakeddit_2
    data_2=cl2(df)
    get_0_data_2=data_2.loc[data_2['Category']==0]
    sorted_2_0=get_0_data_2.groupby("User").size()
    sorted_2_0=sorted_2_0.sort_values(ascending=False)
    sorted_2_0=sorted_2_0[0:5]
    fig = px.bar(x=sorted_2_0.index, y=sorted_2_0)
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="Number of tweets")
    fig.update_layout(showlegend=False)
  
    fig.update_layout(xaxis={'showticklabels': False})    
    graphJSON_2_0 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    get_1_data_2=data_2.loc[data_2['Category']==1]
    sorted_2_1=get_1_data_2.groupby("User").size()
    sorted_2_1=sorted_2_1.sort_values(ascending=False)
    sorted_2_1=sorted_2_1[0:5]
    fig = px.bar(x=sorted_2_1.index, y=sorted_2_1)
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="Number of tweets")
    fig.update_layout(showlegend=False)
   
    fig.update_layout(xaxis={'showticklabels': False})    
    graphJSON_2_1 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON_2_ = []
    
    graphJSON_2_.append(graphJSON_2_0)
    graphJSON_2_.append(graphJSON_2_1)

    
    #fakeddit_6
    data_3 = cl3(df)
    count=[0,0,0,0,0,0]
    

    get_0_data_3=data_3.loc[data_3['Category']==0]
    sorted_3_0=get_0_data_3.groupby("User").size()
    sorted_3_0=sorted_3_0.sort_values(ascending=False)
    sorted_3_0=sorted_3_0[0:5]
    fig = px.bar(x=sorted_3_0.index, y=sorted_3_0)
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="Number of tweets")
    fig.update_layout(showlegend=False)
    #fig.update_layout(yaxis={'visible': False, 'showticklabels': False})
    fig.update_layout(xaxis={'showticklabels': False})    
    graphJSON_3_0 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    get_1_data_3=data_3.loc[data_3['Category']==1]
    sorted_3_1=get_1_data_3.groupby("User").size()
    sorted_3_1=sorted_3_1.sort_values(ascending=False)
    sorted_3_1=sorted_3_1[0:5]
    fig = px.bar(x=sorted_3_1.index, y=sorted_3_1)
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="Number of tweets")
    fig.update_layout(showlegend=False)
    #fig.update_layout(yaxis={'visible': False, 'showticklabels': False})
    fig.update_layout(xaxis={'showticklabels': False})    
    graphJSON_3_1 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    get_2_data_3=data_3.loc[data_3['Category']==2]
    sorted_3_2=get_2_data_3.groupby("User").size()
    sorted_3_2=sorted_3_2.sort_values(ascending=False)
    sorted_3_2=sorted_3_2[0:5]
    fig = px.bar(x=sorted_3_2.index, y=sorted_3_2)
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="Number of tweets")
    fig.update_layout(showlegend=False)
    #fig.update_layout(yaxis={'visible': False, 'showticklabels': False})
    fig.update_layout(xaxis={'showticklabels': False})    
    graphJSON_3_2 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    get_3_data_3=data_3.loc[data_3['Category']==3]
    sorted_3_3=get_3_data_3.groupby("User").size()
    sorted_3_3=sorted_3_3.sort_values(ascending=False)
    sorted_3_3=sorted_3_3[0:5]
    fig = px.bar(x=sorted_3_3.index, y=sorted_3_3)
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="Number of tweets")
    fig.update_layout(showlegend=False)
    #fig.update_layout(yaxis={'visible': False, 'showticklabels': False})
    fig.update_layout(xaxis={'showticklabels': False})    
    graphJSON_3_3 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    get_4_data_3=data_3.loc[data_3['Category']==4]
    sorted_3_4=get_4_data_3.groupby("User").size()
    sorted_3_4=sorted_3_4.sort_values(ascending=False)
    sorted_3_4=sorted_3_4[0:5]
    app.logger.info(sorted_3_4.index)
    app.logger.info(len(sorted_3_4[0:5]))
    app.logger.info('before plotting fig')
    fig = px.bar(x=sorted_3_4.index, y=sorted_3_4)
    app.logger.info('after plotting fig')
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="Number of tweets")
    fig.update_layout(showlegend=False)
    fig.update_layout(xaxis={'showticklabels': False})
    graphJSON_3_4 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    get_5_data_3=data_3.loc[data_3['Category']==5]
    sorted_3_5=get_5_data_3.groupby("User").size()
    sorted_3_5=sorted_3_5.sort_values(ascending=False)
    sorted_3_5=sorted_3_5[0:5]
    app.logger.info(sorted_3_5.index)
    app.logger.info(len(sorted_3_5[0:5]))
    app.logger.info('before plotting fig')
    fig = px.bar(x=sorted_3_5.index, y=sorted_3_5)
    app.logger.info('after plotting fig')
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="Number of tweets")
    fig.update_layout(showlegend=False)
    fig.update_layout(xaxis={'showticklabels': False})
    graphJSON_3_5 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    

    graphJSON_3_ = []
    
    graphJSON_3_.append(graphJSON_3_0)
    graphJSON_3_.append(graphJSON_3_1)
    graphJSON_3_.append(graphJSON_3_2)
    graphJSON_3_.append(graphJSON_3_3)
    graphJSON_3_.append(graphJSON_3_4)
    graphJSON_3_.append(graphJSON_3_5)

    #models.implicit_3
    data_4=cl4(df)
    get_0_data_4=data_4.loc[data_4['Category']==0]
    sorted_4_0=get_0_data_4.groupby("User").size()
    sorted_4_0=sorted_4_0.sort_values(ascending=False)
    sorted_4_0=sorted_4_0[0:5]
    fig = px.bar(x=sorted_4_0.index, y=sorted_4_0)
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="Number of tweets")
    fig.update_layout(showlegend=False)
  
    fig.update_layout(xaxis={'showticklabels': False})    
    graphJSON_4_0 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    get_1_data_4=data_4.loc[data_4['Category']==1]
    sorted_4_1=get_1_data_4.groupby("User").size()
    sorted_4_1=sorted_4_1.sort_values(ascending=False)
    sorted_4_1=sorted_4_1[0:5]
    fig = px.bar(x=sorted_4_1.index, y=sorted_4_1)
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="Number of tweets")
    fig.update_layout(showlegend=False)
   
    fig.update_layout(xaxis={'showticklabels': False})    
    graphJSON_4_1 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    get_2_data_4=data_4.loc[data_4['Category']==2]
    sorted_4_2=get_2_data_4.groupby("User").size()
    sorted_4_2=sorted_4_2.sort_values(ascending=False)
    sorted_4_2=sorted_4_2[0:5]
    fig = px.bar(x=sorted_4_2.index, y=sorted_4_2)
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="Number of tweets")
    fig.update_layout(showlegend=False)
   
    fig.update_layout(xaxis={'showticklabels': False})    
    graphJSON_4_2 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    graphJSON_4_ = []
    
    graphJSON_4_.append(graphJSON_4_0)
    graphJSON_4_.append(graphJSON_4_1)
    graphJSON_4_.append(graphJSON_4_2)

    #models.implicit_5_
    data_5 = cl5(df)
    count=[0,0,0,0,0,0]
   
    

    get_0_data_5=data_5.loc[data_5['Category']==0]
    sorted_5_0=get_0_data_5.groupby("User").size()
    sorted_5_0=sorted_5_0.sort_values(ascending=False)
    sorted_5_0=sorted_5_0[0:5]
    fig = px.bar(x=sorted_5_0.index, y=sorted_5_0)
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="Number of tweets")
    fig.update_layout(showlegend=False)
    #fig.update_layout(yaxis={'visible': False, 'showticklabels': False})
    fig.update_layout(xaxis={'showticklabels': False})    
    graphJSON_5_0 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    get_1_data_5=data_5.loc[data_5['Category']==1]
    sorted_5_1=get_1_data_5.groupby("User").size()
    sorted_5_1=sorted_5_1.sort_values(ascending=False)
    sorted_5_1=sorted_5_1[0:5]
    fig = px.bar(x=sorted_5_1.index, y=sorted_5_1)
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="Number of tweets")
    fig.update_layout(showlegend=False)
    #fig.update_layout(yaxis={'visible': False, 'showticklabels': False})
    fig.update_layout(xaxis={'showticklabels': False})    
    graphJSON_5_1 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    get_2_data_5=data_5.loc[data_5['Category']==2]
    sorted_5_2=get_2_data_5.groupby("User").size()
    sorted_5_2=sorted_5_2.sort_values(ascending=False)
    sorted_5_2=sorted_5_2[0:5]
    fig = px.bar(x=sorted_5_2.index, y=sorted_5_2)
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="Number of tweets")
    fig.update_layout(showlegend=False)
    #fig.update_layout(yaxis={'visible': False, 'showticklabels': False})
    fig.update_layout(xaxis={'showticklabels': False})    
    graphJSON_5_2 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    get_3_data_5=data_5.loc[data_5['Category']==3]
    sorted_5_3=get_3_data_5.groupby("User").size()
    sorted_5_3=sorted_5_3.sort_values(ascending=False)
    sorted_5_3=sorted_5_3[0:5]
    fig = px.bar(x=sorted_5_3.index, y=sorted_5_3)
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="Number of tweets")
    fig.update_layout(showlegend=False)
    #fig.update_layout(yaxis={'visible': False, 'showticklabels': False})
    fig.update_layout(xaxis={'showticklabels': False})    
    graphJSON_5_3 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    get_4_data_5=data_5.loc[data_5['Category']==4]
    sorted_5_4=get_4_data_5.groupby("User").size()
    sorted_5_4=sorted_5_4.sort_values(ascending=False)
    sorted_5_4=sorted_5_4[0:5]
    app.logger.info(sorted_5_4.index)
    app.logger.info(len(sorted_5_4[0:5]))
    app.logger.info('before plotting fig')
    fig = px.bar(x=sorted_5_4.index, y=sorted_5_4)
    app.logger.info('after plotting fig')
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="Number of tweets")
    fig.update_layout(showlegend=False)
    fig.update_layout(xaxis={'showticklabels': False})
    graphJSON_5_4 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    get_5_data_5=data_5.loc[data_5['Category']==5]
    sorted_5_5=get_5_data_5.groupby("User").size()
    sorted_5_5=sorted_5_5.sort_values(ascending=False)
    sorted_5_5=sorted_5_5[0:5]
    app.logger.info(sorted_5_5.index)
    app.logger.info(len(sorted_5_5[0:5]))
    app.logger.info('before plotting fig')
    fig = px.bar(x=sorted_5_5.index, y=sorted_5_5)
    app.logger.info('after plotting fig')
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="Number of tweets")
    fig.update_layout(showlegend=False)
    fig.update_layout(xaxis={'showticklabels': False})
    graphJSON_5_5 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    

    graphJSON_5_ = []
    
    graphJSON_5_.append(graphJSON_5_0)
    graphJSON_5_.append(graphJSON_5_1)
    graphJSON_5_.append(graphJSON_5_2)
    graphJSON_5_.append(graphJSON_5_3)
    graphJSON_5_.append(graphJSON_5_4)
    graphJSON_5_.append(graphJSON_5_5)

    

    return graphJSON_1_,graphJSON_2_,graphJSON_3_,graphJSON_4_,graphJSON_5_