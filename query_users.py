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
    data = cl3(df)
    count=[0,0,0,0,0,0]
    for i in range(len(count)):
        count[i]=len(data.loc[data['Category']==i])


    #data2=cl3(df)
    for i in count:
        app.logger.info("count")
        app.logger.info(i)
    #app.logger.info(data2.loc[0])
    

    get_0_data=data.loc[data['Category']==0]
    sorted_0=get_0_data.groupby("User").size()
    sorted_0=sorted_0.sort_values(ascending=False)
    sorted_0=sorted_0[0:5]
    fig = px.bar(x=sorted_0.index, y=sorted_0)
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="# tweets")
    fig.update_layout(showlegend=False)
    #fig.update_layout(yaxis={'visible': False, 'showticklabels': False})
    fig.update_layout(xaxis={'showticklabels': False})    
    graphJSON0 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    '''
    get_1_data=data.loc[data['Category']==1]
    sorted_1=get_1_data.groupby("User").size()
    sorted_1=sorted_1.sort_values(ascending=False)
    sorted_1=sorted_1[0:5]
    fig = px.bar(x=sorted_1.index, y=sorted_1)
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="# tweets")
    fig.update_layout(showlegend=False)
    #fig.update_layout(yaxis={'visible': False, 'showticklabels': False})
    fig.update_layout(xaxis={'showticklabels': False})    
    graphJSON1 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    '''
    get_2_data=data.loc[data['Category']==2]
    sorted_2=get_2_data.groupby("User").size()
    sorted_2=sorted_2.sort_values(ascending=False)
    sorted_2=sorted_2[0:5]
    fig = px.bar(x=sorted_2.index, y=sorted_2)
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="# tweets")
    fig.update_layout(showlegend=False)
    #fig.update_layout(yaxis={'visible': False, 'showticklabels': False})
    fig.update_layout(xaxis={'showticklabels': False})    
    graphJSON2 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    get_3_data=data.loc[data['Category']==3]
    sorted_3=get_3_data.groupby("User").size()
    sorted_3=sorted_3.sort_values(ascending=False)
    sorted_3=sorted_3[0:5]
    fig = px.bar(x=sorted_3.index, y=sorted_3)
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="# tweets")
    fig.update_layout(showlegend=False)
    #fig.update_layout(yaxis={'visible': False, 'showticklabels': False})
    fig.update_layout(xaxis={'showticklabels': False})    
    graphJSON3 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    get_4_data=data.loc[data['Category']==4]
    sorted_4=get_4_data.groupby("User").size()
    sorted_4=sorted_4.sort_values(ascending=False)
    sorted_4=sorted_4[0:5]
    app.logger.info(sorted_4.index)
    app.logger.info(len(sorted_4[0:5]))
    app.logger.info('before plotting fig')
    fig = px.bar(x=sorted_4.index, y=sorted_4)
    app.logger.info('after plotting fig')
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="# tweets")
    fig.update_layout(showlegend=False)
    fig.update_layout(xaxis={'showticklabels': False})
    graphJSON4 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    get_5_data=data.loc[data['Category']==5]
    sorted_5=get_5_data.groupby("User").size()
    sorted_5=sorted_5.sort_values(ascending=False)
    sorted_5=sorted_5[0:5]
    app.logger.info(sorted_5.index)
    app.logger.info(len(sorted_5[0:5]))
    app.logger.info('before plotting fig')
    fig = px.bar(x=sorted_5.index, y=sorted_5)
    app.logger.info('after plotting fig')
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="# tweets")
    fig.update_layout(showlegend=False)
    fig.update_layout(xaxis={'showticklabels': False})
    graphJSON5 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    sorted_likes_count_0=get_0_data.drop_duplicates("User")
    sorted_likes_count_0=sorted_likes_count_0.sort_values("Likes",ascending=False)
    app.logger.info("count_likes 0")
    app.logger.info(len(sorted_likes_count_0))
    sorted_likes_count_0=sorted_likes_count_0[0:5]
    fig = px.bar(x=sorted_likes_count_0["User"], y=sorted_likes_count_0["Likes"])
    app.logger.info('after plotting fig')
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="# Likes")
    fig.update_layout(showlegend=False)
    fig.update_layout(xaxis={'showticklabels': False})
    graphJSON_likes_0 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    '''
    sorted_likes_count_1=get_1_data.drop_duplicates("User")
    sorted_likes_count_1=sorted_likes_count_1.sort_values("Likes",ascending=False)
    sorted_likes_count_1=sorted_likes_count_1[0:5]
    app.logger.info("count likes 1")
    app.logger.info(len(sorted_likes_count_1))
    fig = px.bar(x=sorted_likes_count_1["User"], y=sorted_likes_count_1["Likes"])
    app.logger.info('after plotting fig')
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="# Likes")
    fig.update_layout(showlegend=False)
    fig.update_layout(xaxis={'showticklabels': False})
    graphJSON_likes_1 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    '''
    sorted_likes_count_2=get_2_data.drop_duplicates("User")
    sorted_likes_count_2=sorted_likes_count_2.sort_values("Likes",ascending=False)
    app.logger.info("count_likes 2")
    app.logger.info(len(sorted_likes_count_2))
    sorted_likes_count_2=sorted_likes_count_2[0:5]
    fig = px.bar(x=sorted_likes_count_2["User"], y=sorted_likes_count_2["Likes"])
    app.logger.info('after plotting fig')
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="# Likes")
    fig.update_layout(showlegend=False)
    fig.update_layout(xaxis={'showticklabels': False})
    graphJSON_likes_2 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    sorted_likes_count_3=get_3_data.drop_duplicates("User")
    sorted_likes_count_3=sorted_likes_count_3.sort_values("Likes",ascending=False)
    app.logger.info("count_likes 3")
    app.logger.info(len(sorted_likes_count_3))
    sorted_likes_count_3=sorted_likes_count_3[0:5]
    fig = px.bar(x=sorted_likes_count_3["User"], y=sorted_likes_count_3["Likes"])
    app.logger.info('after plotting fig')
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="# Likes")
    fig.update_layout(showlegend=False)
    fig.update_layout(xaxis={'showticklabels': False})
    graphJSON_likes_3 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    sorted_likes_count_4=get_4_data.drop_duplicates("User")
    sorted_likes_count_4=sorted_likes_count_4.sort_values("Likes",ascending=False)
    app.logger.info("count_likes 4")
    app.logger.info(len(sorted_likes_count_4))
    sorted_likes_count_4=sorted_likes_count_4[0:5]
    fig = px.bar(x=sorted_likes_count_4["User"], y=sorted_likes_count_4["Likes"])
    app.logger.info('after plotting fig')
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="# Likes")
    fig.update_layout(showlegend=False)
    fig.update_layout(xaxis={'showticklabels': False})
    graphJSON_likes_4 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    sorted_likes_count_5=get_5_data.drop_duplicates("User")
    sorted_likes_count_5=sorted_likes_count_5.sort_values("Likes",ascending=False)
    app.logger.info("count_likes 5")
    app.logger.info(len(sorted_likes_count_5))
    sorted_likes_count_5=sorted_likes_count_5[0:5]
    fig = px.bar(x=sorted_likes_count_5["User"], y=sorted_likes_count_5["Likes"])
    app.logger.info('after plotting fig')
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="# Likes")
    fig.update_layout(showlegend=False)
    fig.update_layout(xaxis={'showticklabels': False})
    graphJSON_likes_5 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    graphJSON = []
    graphJSON_likes = []
    graphJSON.append(graphJSON0)
    graphJSON.append(graphJSON0)
    graphJSON.append(graphJSON2)
    graphJSON.append(graphJSON3)
    graphJSON.append(graphJSON4)
    graphJSON.append(graphJSON5)
    graphJSON_likes.append(graphJSON_likes_0)
    graphJSON_likes.append(graphJSON_likes_0)
    graphJSON_likes.append(graphJSON_likes_2)
    graphJSON_likes.append(graphJSON_likes_3)
    graphJSON_likes.append(graphJSON_likes_4)
    graphJSON_likes.append(graphJSON_likes_5)

    return graphJSON, graphJSON_likes