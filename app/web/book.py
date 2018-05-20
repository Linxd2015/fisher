import json

from flask import jsonify, request
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookViewModel, BookCollection
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
    books = BookCollection()

    # validate返回为真则表示验证通过
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, q)
        return json.dumps(books, default=lambda o: o.__dict__)
    else:
        return jsonify(form.errors)