from flask import Flask,request,jsonify

app = Flask(__name__)

posts = [
    {'id':1,'title':'hello','body':'world'},
    {'id':2,'title':'Test','body':'framework'}
]


@app.route('/posts',methods=['GET'])
def get_posts():
    return jsonify(posts),200
@app.route('/posts/<int:post_id>',methods=['GET'])
def get_single_data(post_id):
    post = next((i for i in posts if i['id']==post_id),None)
    return jsonify(post) if post else ('Not found',404)

@app.route('/posts',methods=['POST'])
def create_post():
    data = request.json
    new_id = max(i['id'] for i in posts)+1 if posts else 1
    new_post = {'id':new_id,'title':data['title'],'body':data['body']}
    posts.append(new_post)
    return jsonify(new_post),201



if __name__ == '__main__':
    app.run(debug=True)

