from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('plag.html')

@app.route('/', methods = ['POST'])
def my_form_post():
    file1 = request.form['txt']
    file2 = request.form['text']
    count = 0
    
    filelist1=file1.encode('utf8')
    filelist2 = file2.encode('utf8')

    # stopwords=['is','are','and']
    # for i in range(len(stopwords)):
    #    foo = foo.replace(stopwords[i],' ')

    foo = filelist1.replace('.',' ')
    bar = filelist2.replace('.', ' ')
    foo= foo.replace(',',' ')
    foo = foo.replace(';', ' ')
    bar = bar.replace(',', ' ')
    bar = bar.replace(';', ' ')
    filelist1= foo
    filelist2 = bar
    filelist1=filelist1.split(' ')
    filelist2=filelist2.split(' ')

    #print filelist1, filelist2
    same_words= set(filelist1) & set(filelist2)  #keyword 'set'|set1 & set2:find common words using set intersection(A /\ B)
    count=len(same_words)


    similarity_ratio1= float(count)/len(filelist1)
    similarity_ratio2= float(count)/len(filelist2)
    mean_ratio=  (similarity_ratio1+similarity_ratio2)/2
    similarity_ratio=mean_ratio*100
    #print type(similarity_ratio)

    if similarity_ratio > 69:  
        return '<h1>plagarism has BEEN detected with documents being ' + str(similarity_ratio) + '% similar'
    else:
        return '<h1>plagarism has NOT BEEN detected with documents being ' + str(similarity_ratio) + '% similar'


if __name__ == '__main__':
    app.run()
