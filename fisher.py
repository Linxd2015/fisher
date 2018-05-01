from app import create_app


__author__ = '七月'

app = create_app()

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])