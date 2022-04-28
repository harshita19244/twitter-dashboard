import json
import plotly
import plotly.express as px
from models.hsol import caller as cl1
from models.fakeddit_2 import caller as cl2
from models.fakeddit_6 import caller as cl3
from models.implicit_3 import caller as cl4
from models.implicit_6 import caller as cl5

labels1= [0,0]
labels2= [0,0,0,0,0,0]
labels3= [0,0,0]
labels4= [0,0,0,0,0,0]

def plot_bargraph(df):
    pred = cl2(df)
    pred= pred['Category']
    # print("printing predictions")
    # print(pred)
    for i in range(0,len(pred)):
        pp= pred[i]
        labels1[pp]=labels1[pp]+1
    print(labels1)
    x_axis1= ['Fake', 'Not Fake']
    fig = px.bar(x=x_axis1, y=labels1,width=400, height=500, color=['cyan','red'],labels={'x':'Category', 'y':'Categorical_Count'})
    fig.update_layout(
    xaxis_title="Category",
    yaxis_title="Categorical_Count"
)
    fig.update_layout(showlegend=False)
    graphJSON1 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    pred = cl3(df)
    pred= pred['Category']
    # print("printing predictions")
    # print(pred)
    for i in range(0,len(pred)):
        pp= pred[i]
        labels2[pp]=labels2[pp]+1
    print(labels2)
    x_axis2= ['Grievance', 'Incitement', 'Threats', 'Irony', 'Stereotypes', 'Inferiority']
    fig = px.bar(x=x_axis2, y=labels2,width=400, height=500, color=['cyan','red','purple','green', 'blue', 'black'],labels={'x':'Category', 'y':'Categorical_Count'})
    fig.update_layout(showlegend=False)
    fig.update_layout(
    xaxis_title="Category",
    yaxis_title="Categorical_Count"
)
    graphJSON2 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    pred = cl4(df)
    pred= pred['Category']
    print("printing predictions")
    print(pred)
    for i in range(0,len(pred)):
        pp= pred[i]
        labels3[pp]=labels3[pp]+1
    print(labels2)
    x_axis3= ['Expicit', 'Implicit','Not Hate']
    fig = px.bar(x=x_axis3, y=labels3,width=400, height=500, color=['cyan','red','purple'],labels={'x':'Category', 'y':'Categorical_Count'})
    fig.update_layout(showlegend=False)
    fig.update_layout(
    xaxis_title="Category",
    yaxis_title="Categorical_Count"
)
    graphJSON3 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    pred = cl5(df)
    pred= pred['Category']
    print("printing predictions")
    print(pred)
    for i in range(0,len(pred)):
        pp= pred[i]
        labels4[pp]=labels4[pp]+1
    print(labels4)
    x_axis4= [ "incitement" ,"inferiority" , "irony" , "stereotypical" , "threatening" ,"white grievance"]
    fig = px.bar(x=x_axis4, y=labels4,width=400, height=500, color=['cyan','red','purple','green', 'blue', 'black'],labels={'x':'Category', 'y':'Categorical_Count'})
    fig.update_layout(showlegend=False)
    fig.update_layout(
    xaxis_title="Category",
    yaxis_title="Categorical_Count"
)
    graphJSON4 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    # return render_template('index.html', name = 'wordcloud_plot', url ='/static/images/wordcloud_plot.png')

    graphJSON = []
    graphJSON.append(graphJSON1)
    graphJSON.append(graphJSON2)
    graphJSON.append(graphJSON3)
    graphJSON.append(graphJSON4)
    return graphJSON