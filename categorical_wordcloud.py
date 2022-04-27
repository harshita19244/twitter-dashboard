
from sqlalchemy import false
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from models.hsol import caller as cl1
from models.fakeddit_2 import caller as cl2
from models.fakeddit_6 import caller as cl3
from models.implicit_3 import caller as cl4
from models.implicit_6 import caller as cl5


urls = []
names = []

def hsol_create(pred):
    hate_tweets = pred.loc[pred['Category'] == 0]
    offensive_tweets = pred.loc[pred['Category'] == 1]
    none_tweets = pred.loc[pred['Category'] == 2]
    print(hate_tweets)
    pil_imgh = WordCloud(collocations = False, background_color = 'white').generate(' '.join(hate_tweets['Tweet']))
    pil_imgh2 = WordCloud(collocations = False, background_color = 'white').generate(' '.join(offensive_tweets['Tweet']))
    pil_imgh3 = WordCloud(collocations = False, background_color = 'white').generate(' '.join(none_tweets['Tweet']))
    plt.imshow(pil_imgh, interpolation='bilinear')
    plt.axis("off")
    plt.savefig('./static/images/wh_1.png')
    plt.imshow(pil_imgh2, interpolation='bilinear')
    plt.axis("off")
    plt.savefig('./static/images/wh_2.png')
    plt.imshow(pil_imgh3, interpolation='bilinear')
    plt.axis("off")
    plt.savefig('./static/images/wh_3.png')
    names.append(pil_imgh);names.append(pil_imgh2);names.append(pil_imgh3)
    urls.append('./static/images/wh_1.png');urls.append('./static/images/wh_2.png');urls.append('./static/images/wh_3.png')



def implicit3_create(pred):
    hate_tweets = pred.loc[pred['Category'] == 0]
    offensive_tweets = pred.loc[pred['Category'] == 1]
    none_tweets = pred.loc[pred['Category'] == 2]
    print(hate_tweets)
    pil_img = WordCloud(collocations = False, background_color = 'white').generate(' '.join(hate_tweets['Tweet']))
    pil_img2 = WordCloud(collocations = False, background_color = 'white').generate(' '.join(offensive_tweets['Tweet']))
    pil_img3 = WordCloud(collocations = False, background_color = 'white').generate(' '.join(none_tweets['Tweet']))
    plt.imshow(pil_img, interpolation='bilinear')
    plt.axis("off")
    plt.savefig('./static/images/wordcloud_plot1.png')
    plt.imshow(pil_img2, interpolation='bilinear')
    plt.axis("off")
    plt.savefig('./static/images/wordcloud_plot2.png')
    plt.imshow(pil_img3, interpolation='bilinear')
    plt.axis("off")
    plt.savefig('./static/images/wordcloud_plot3.png')
    names.append(pil_img);names.append(pil_img2);names.append(pil_img3)
    urls.append()

def implicit6_create(pred):
    hate_tweets = pred.loc[pred['Category'] == 0]
    offensive_tweets = pred.loc[pred['Category'] == 1]
    none_tweets = pred.loc[pred['Category'] == 2]
    print(hate_tweets)
    pil_img = WordCloud(collocations = False, background_color = 'white').generate(' '.join(hate_tweets['Tweet']))
    pil_img2 = WordCloud(collocations = False, background_color = 'white').generate(' '.join(offensive_tweets['Tweet']))
    pil_img3 = WordCloud(collocations = False, background_color = 'white').generate(' '.join(none_tweets['Tweet']))
    plt.imshow(pil_img, interpolation='bilinear')
    plt.axis("off")
    plt.savefig('./static/images/wordcloud_plot1.png')
    plt.imshow(pil_img2, interpolation='bilinear')
    plt.axis("off")
    plt.savefig('./static/images/wordcloud_plot2.png')
    plt.imshow(pil_img3, interpolation='bilinear')
    plt.axis("off")
    plt.savefig('./static/images/wordcloud_plot3.png')
    names.append(pil_img);names.append(pil_img2);names.append(pil_img3)
    urls.append()


def fakeddit2_create(pred):
    true_tweets = pred.loc[pred['Category'] == 0]
    fake_tweets = pred.loc[pred['Category'] == 1]
    pil_imgf = WordCloud(collocations = False, background_color = 'white').generate(' '.join(true_tweets['Tweet']))
    pil_imgf2 = WordCloud(collocations = False, background_color = 'white').generate(' '.join(fake_tweets['Tweet']))
    plt.imshow(pil_imgf, interpolation='bilinear')
    plt.axis("off")
    plt.savefig('./static/images/wf2_1.png')
    plt.imshow(pil_imgf2, interpolation='bilinear')
    plt.axis("off")
    plt.savefig('./static/images/wf2_2.png')
    names.append(pil_imgf);names.append(pil_imgf2)
    urls.append('./static/images/wf2_1.png');urls.append('./static/images/wf2_2.png')

def fakeddit6_create(pred):
    true_tweets = pred.loc[pred['Category'] == 0]
    satire_tweets = pred.loc[pred['Category'] == 1]
    misleading_tweets = pred.loc[pred['Category'] == 2]
    false_tweets = pred.loc[pred['Category'] == 3]
    imposter_tweets = pred.loc[pred['Category'] == 4]
    manipulated_tweets = pred.loc[pred['Category'] == 5]
    pil_img = WordCloud(collocations = False, background_color = 'white').generate(' '.join(true_tweets['Tweet']))
    pil_img2 = WordCloud(collocations = False, background_color = 'white').generate(' '.join(satire_tweets['Tweet']))
    pil_img3 = WordCloud(collocations = False, background_color = 'white').generate(' '.join(misleading_tweets['Tweet']))
    pil_img4 = WordCloud(collocations = False, background_color = 'white').generate(' '.join(false_tweets['Tweet']))
    pil_img5 = WordCloud(collocations = False, background_color = 'white').generate(' '.join(imposter_tweets['Tweet']))
    pil_img6 = WordCloud(collocations = False, background_color = 'white').generate(' '.join(manipulated_tweets['Tweet']))
    plt.imshow(pil_img, interpolation='bilinear')
    plt.axis("off")
    plt.savefig('./static/images/wf6_1.png')
    plt.imshow(pil_img2, interpolation='bilinear')
    plt.axis("off")
    plt.savefig('./static/images/wf6_2.png')
    plt.imshow(pil_img3, interpolation='bilinear')
    plt.axis("off")
    plt.savefig('./static/images/wf6_3.png')
    plt.imshow(pil_img4, interpolation='bilinear')
    plt.axis("off")
    plt.savefig('./static/images/wf6_4.png')
    plt.imshow(pil_img5, interpolation='bilinear')
    plt.axis("off")
    plt.savefig('./static/images/wf6_5.png')
    plt.imshow(pil_img6, interpolation='bilinear')
    plt.axis("off")
    plt.savefig('./static/images/wf6_6.png')
    urls.append('./static/images/wf6_1.png');urls.append('./static/images/wf6_2.png');urls.append('./static/images/wf6_3.png');urls.append('./static/images/wf6_4.png')
    urls.append('./static/images/wf6_5.png');urls.append('./static/images/wf6_5.png')
    names.append(pil_img);names.append(pil_img2);names.append(pil_img3);names.append(pil_img4);names.append(pil_img5);names.append(pil_img6)


def create_wordcloud(df):
    #using hsol
    hsol_create(cl1(df))
    fakeddit2_create(cl2(df))
    #fakeddit6_create(cl3(df))
    #implicit3_create(cl4(df))
    #implicit6_create(cl5(df))
    return names,urls

