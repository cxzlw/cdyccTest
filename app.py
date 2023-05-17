import sanic
from sanic import Sanic
from sanic.response import text
import zhihuDecrypt as zhihu

app = Sanic("cdyccTest")


@app.route("/")
async def index(request: sanic.Request):
    if "id" not in request.args:
        return text("You have not passed any arguments here. Usage: url/id=xxxxx")
    c = zhihu.get_cdycc(request.args.get("id"))
    return text(zhihu.decrypt(c, zhihu.detect_encrypt_method(c)))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=18668)
