from flask import jsonify, request
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from . import web
from app.foms.book import SearchForm


@web.route('/book/search')
def search():
    """
        搜索api需要参数
        q : 普通关键字和isbn
        page : 由start和count决定
        使用request实现->?q=金庸&page=1的请求
    """
    form = SearchForm(request.args)
    # validate返回为真则表示验证通过
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q)
        # return json.dumps(result), 200, {'content-type':'application/json'}
        return jsonify(result)
    else:
        return jsonify({'msg': '参数校验失败'})