{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":32,"position":32,"stack":[[{"start":{"row":0,"column":0},"end":{"row":14,"column":0},"action":"insert","lines":["# app.py","import flask","import os","","app = flask.Flask(__name__)","","@app.route('/') ","def index(): ","    return \"Hello, world!\"","    ","app.run(","    port=int(os.getenv('PORT', 8080)),","    host=os.getenv('IP', '0.0.0.0')",")",""],"id":1}],[{"start":{"row":12,"column":35},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "]},{"start":{"row":13,"column":4},"end":{"row":13,"column":5},"action":"insert","lines":["f"]},{"start":{"row":13,"column":5},"end":{"row":13,"column":6},"action":"insert","lines":["r"]}],[{"start":{"row":13,"column":5},"end":{"row":13,"column":6},"action":"remove","lines":["r"],"id":3},{"start":{"row":13,"column":4},"end":{"row":13,"column":5},"action":"remove","lines":["f"]},{"start":{"row":13,"column":4},"end":{"row":13,"column":5},"action":"insert","lines":["d"]},{"start":{"row":13,"column":5},"end":{"row":13,"column":6},"action":"insert","lines":["e"]},{"start":{"row":13,"column":6},"end":{"row":13,"column":7},"action":"insert","lines":["b"]},{"start":{"row":13,"column":7},"end":{"row":13,"column":8},"action":"insert","lines":["i"]}],[{"start":{"row":13,"column":7},"end":{"row":13,"column":8},"action":"remove","lines":["i"],"id":4}],[{"start":{"row":13,"column":7},"end":{"row":13,"column":8},"action":"insert","lines":["j"],"id":5},{"start":{"row":13,"column":8},"end":{"row":13,"column":9},"action":"insert","lines":["u"]}],[{"start":{"row":13,"column":8},"end":{"row":13,"column":9},"action":"remove","lines":["u"],"id":6},{"start":{"row":13,"column":7},"end":{"row":13,"column":8},"action":"remove","lines":["j"]}],[{"start":{"row":13,"column":7},"end":{"row":13,"column":8},"action":"insert","lines":["u"],"id":7},{"start":{"row":13,"column":8},"end":{"row":13,"column":9},"action":"insert","lines":["g"]},{"start":{"row":13,"column":9},"end":{"row":13,"column":10},"action":"insert","lines":["="]},{"start":{"row":13,"column":10},"end":{"row":13,"column":11},"action":"insert","lines":["T"]},{"start":{"row":13,"column":11},"end":{"row":13,"column":12},"action":"insert","lines":["t"]},{"start":{"row":13,"column":12},"end":{"row":13,"column":13},"action":"insert","lines":["r"]}],[{"start":{"row":13,"column":12},"end":{"row":13,"column":13},"action":"remove","lines":["r"],"id":8},{"start":{"row":13,"column":11},"end":{"row":13,"column":12},"action":"remove","lines":["t"]}],[{"start":{"row":13,"column":11},"end":{"row":13,"column":12},"action":"insert","lines":["r"],"id":9},{"start":{"row":13,"column":12},"end":{"row":13,"column":13},"action":"insert","lines":["u"]},{"start":{"row":13,"column":13},"end":{"row":13,"column":14},"action":"insert","lines":["e"]}],[{"start":{"row":12,"column":35},"end":{"row":12,"column":36},"action":"insert","lines":[","],"id":10},{"start":{"row":12,"column":36},"end":{"row":12,"column":37},"action":"insert","lines":["."]}],[{"start":{"row":12,"column":36},"end":{"row":12,"column":37},"action":"remove","lines":["."],"id":11}],[{"start":{"row":15,"column":0},"end":{"row":15,"column":1},"action":"insert","lines":["z"],"id":12}],[{"start":{"row":15,"column":0},"end":{"row":15,"column":1},"action":"remove","lines":["z"],"id":13}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":26},"action":"remove","lines":["    return \"Hello, world!\""],"id":14},{"start":{"row":8,"column":0},"end":{"row":8,"column":46},"action":"insert","lines":["    return flask.render_template(\"index.html\")"]}],[{"start":{"row":14,"column":1},"end":{"row":15,"column":0},"action":"remove","lines":["",""],"id":15}],[{"start":{"row":8,"column":12},"end":{"row":8,"column":46},"action":"remove","lines":["lask.render_template(\"index.html\")"],"id":16},{"start":{"row":8,"column":11},"end":{"row":8,"column":12},"action":"remove","lines":["f"]}],[{"start":{"row":8,"column":11},"end":{"row":8,"column":13},"action":"insert","lines":["\"\""],"id":17}],[{"start":{"row":8,"column":11},"end":{"row":8,"column":13},"action":"remove","lines":["\"\""],"id":18}],[{"start":{"row":8,"column":11},"end":{"row":8,"column":12},"action":"insert","lines":["p"],"id":19},{"start":{"row":8,"column":12},"end":{"row":8,"column":13},"action":"insert","lines":["r"]},{"start":{"row":8,"column":13},"end":{"row":8,"column":14},"action":"insert","lines":["i"]},{"start":{"row":8,"column":14},"end":{"row":8,"column":15},"action":"insert","lines":["n"]},{"start":{"row":8,"column":15},"end":{"row":8,"column":16},"action":"insert","lines":["t"]},{"start":{"row":8,"column":16},"end":{"row":8,"column":17},"action":"insert","lines":["9"]}],[{"start":{"row":8,"column":16},"end":{"row":8,"column":17},"action":"remove","lines":["9"],"id":20},{"start":{"row":8,"column":15},"end":{"row":8,"column":16},"action":"remove","lines":["t"]},{"start":{"row":8,"column":14},"end":{"row":8,"column":15},"action":"remove","lines":["n"]},{"start":{"row":8,"column":13},"end":{"row":8,"column":14},"action":"remove","lines":["i"]},{"start":{"row":8,"column":12},"end":{"row":8,"column":13},"action":"remove","lines":["r"]},{"start":{"row":8,"column":11},"end":{"row":8,"column":12},"action":"remove","lines":["p"]}],[{"start":{"row":8,"column":11},"end":{"row":8,"column":13},"action":"insert","lines":["\"\""],"id":21}],[{"start":{"row":8,"column":12},"end":{"row":8,"column":13},"action":"insert","lines":["h"],"id":22},{"start":{"row":8,"column":13},"end":{"row":8,"column":14},"action":"insert","lines":["e"]},{"start":{"row":8,"column":14},"end":{"row":8,"column":15},"action":"insert","lines":["l"]},{"start":{"row":8,"column":15},"end":{"row":8,"column":16},"action":"insert","lines":["l"]},{"start":{"row":8,"column":16},"end":{"row":8,"column":17},"action":"insert","lines":["o"]}],[{"start":{"row":8,"column":17},"end":{"row":8,"column":18},"action":"insert","lines":[" "],"id":23},{"start":{"row":8,"column":18},"end":{"row":8,"column":19},"action":"insert","lines":["w"]},{"start":{"row":8,"column":19},"end":{"row":8,"column":20},"action":"insert","lines":["o"]},{"start":{"row":8,"column":20},"end":{"row":8,"column":21},"action":"insert","lines":["r"]},{"start":{"row":8,"column":21},"end":{"row":8,"column":22},"action":"insert","lines":["l"]},{"start":{"row":8,"column":22},"end":{"row":8,"column":23},"action":"insert","lines":["d"]}],[{"start":{"row":8,"column":3},"end":{"row":8,"column":24},"action":"remove","lines":[" return \"hello world\""],"id":24},{"start":{"row":8,"column":2},"end":{"row":8,"column":3},"action":"remove","lines":[" "]},{"start":{"row":8,"column":1},"end":{"row":8,"column":2},"action":"remove","lines":[" "]},{"start":{"row":8,"column":0},"end":{"row":8,"column":1},"action":"remove","lines":[" "]},{"start":{"row":7,"column":13},"end":{"row":8,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":7,"column":13},"end":{"row":8,"column":0},"action":"insert","lines":["",""],"id":25},{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":8,"column":4},"end":{"row":8,"column":46},"action":"insert","lines":["return flask.render_template(\"index.html\")"],"id":26}],[{"start":{"row":8,"column":34},"end":{"row":8,"column":35},"action":"remove","lines":["i"],"id":27},{"start":{"row":8,"column":33},"end":{"row":8,"column":34},"action":"remove","lines":["\""]}],[{"start":{"row":8,"column":33},"end":{"row":8,"column":38},"action":"insert","lines":["index"],"id":28}],[{"start":{"row":8,"column":35},"end":{"row":8,"column":48},"action":"remove","lines":["dexndex.html\""],"id":29},{"start":{"row":8,"column":34},"end":{"row":8,"column":35},"action":"remove","lines":["n"]},{"start":{"row":8,"column":33},"end":{"row":8,"column":34},"action":"remove","lines":["i"]}],[{"start":{"row":8,"column":33},"end":{"row":8,"column":34},"action":"remove","lines":[")"],"id":30},{"start":{"row":8,"column":33},"end":{"row":8,"column":35},"action":"insert","lines":["\"\""]}],[{"start":{"row":8,"column":34},"end":{"row":8,"column":35},"action":"remove","lines":["\""],"id":31},{"start":{"row":8,"column":34},"end":{"row":8,"column":35},"action":"insert","lines":["i"]},{"start":{"row":8,"column":35},"end":{"row":8,"column":36},"action":"insert","lines":["n"]},{"start":{"row":8,"column":36},"end":{"row":8,"column":37},"action":"insert","lines":["d"]},{"start":{"row":8,"column":37},"end":{"row":8,"column":38},"action":"insert","lines":["e"]},{"start":{"row":8,"column":38},"end":{"row":8,"column":39},"action":"insert","lines":["x"]},{"start":{"row":8,"column":39},"end":{"row":8,"column":40},"action":"insert","lines":["."]},{"start":{"row":8,"column":40},"end":{"row":8,"column":41},"action":"insert","lines":["h"]},{"start":{"row":8,"column":41},"end":{"row":8,"column":42},"action":"insert","lines":["t"]},{"start":{"row":8,"column":42},"end":{"row":8,"column":43},"action":"insert","lines":["m"]}],[{"start":{"row":8,"column":43},"end":{"row":8,"column":44},"action":"insert","lines":["l"],"id":32}],[{"start":{"row":8,"column":44},"end":{"row":8,"column":45},"action":"insert","lines":["\""],"id":33},{"start":{"row":8,"column":45},"end":{"row":8,"column":46},"action":"insert","lines":[")"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":4,"column":27},"end":{"row":4,"column":27},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1567807347008,"hash":"fdcbb5bc564bef7a587132c068ef3650200bfa1e"}