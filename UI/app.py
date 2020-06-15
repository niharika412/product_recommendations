import rect
import dash
import os
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
imgs_path = "imgs/"
imgs_model_width, imgs_model_height = 224, 224

nb_closest_images = 5
#files from local directory

files = [imgs_path + x for x in os.listdir(imgs_path) if "jpeg" in x]
# the style arguments for the top. We use position:fixed and a fixed width
TOP_STYLE= {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "height": "70%",
	"width":"100%",
    "padding": "2rem 1rem",
    "background-color": "#12343b",
	"overflow" :'scroll',
	'font-family':'Ink Free',
	"color": '#fff'
}

# the styles for the main content position it to the right of the top and
# add some padding.
CONTENT_STYLE = {
    "padding": "2rem 1rem",
	"margin-top": "35%",
	"color": '#000',
	"background-color": "#c89666",
	'font-family':'Ink Free'
	
}

#designing the top of the UI to display images

top = html.Div(
    [
        html.H2("Product Recommendations", className="display-4"),
        html.Hr(style={'border-top': '1px solid white'}),
        html.P(
            "Click on a product to get recommendations", className="lead"
        ),
		dbc.Row(
		[
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/0.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}), color="light",id="a", className="m-1",n_clicks_timestamp=1)),
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/1.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='b', color="light", className="m-1",n_clicks_timestamp=1)),
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/10.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='c', color="light", className="m-1",n_clicks_timestamp=1)),
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/11.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='d', color="light", className="m-1",n_clicks_timestamp=1)),
		dbc.Col(
		dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/12.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='e', color="light", className="m-1",n_clicks_timestamp=1)),
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/13.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='f', color="light", className="m-1",n_clicks_timestamp=1)),
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/14.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='g', color="light", className="m-1",n_clicks_timestamp=1)),
		
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/15.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='h', color="light", className="m-1",n_clicks_timestamp=1)),
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/16.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='i', color="light", className="m-1",n_clicks_timestamp=1)),
		
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/17.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='j', color="light", className="m-1",n_clicks_timestamp=1)),
		
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/18.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='k', color="light", className="m-1",n_clicks_timestamp=1)),
		
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/19.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='l', color="light", className="m-1",n_clicks_timestamp=1)),
		
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/2.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='m', color="light", className="m-1",n_clicks_timestamp=1)),
		
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/20.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='n', color="light", className="m-1",n_clicks_timestamp=1)),
		
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/21.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='o', color="light", className="m-1",n_clicks_timestamp=1)),
		
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/22.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='p', color="light", className="m-1",n_clicks_timestamp=1)),
		
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/23.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='q', color="light", className="m-1",n_clicks_timestamp=1)),
		
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/24.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='r', color="light", className="m-1",n_clicks_timestamp=1)),
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/25.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='s', color="light", className="m-1",n_clicks_timestamp=1)),
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/26.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='t', color="light", className="m-1",n_clicks_timestamp=1)),
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/27.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='u', color="light", className="m-1",n_clicks_timestamp=1)),
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/28.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='v', color="light", className="m-1",n_clicks_timestamp=1)),
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/29.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='w', color="light", className="m-1",n_clicks_timestamp=1)),
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/3.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='x', color="light", className="m-1",n_clicks_timestamp=1)),
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/30.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='y', color="light", className="m-1",n_clicks_timestamp=1)),
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/31.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='z', color="light", className="m-1",n_clicks_timestamp=1)),
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/32.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='aa', color="light", className="m-1",n_clicks_timestamp=1)),
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/33.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='ab', color="light", className="m-1",n_clicks_timestamp=1)),
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/34.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='ac', color="light", className="m-1",n_clicks_timestamp=1)),
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/35.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='ad', color="light", className="m-1",n_clicks_timestamp=1)),
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/36.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='ae', color="light", className="m-1",n_clicks_timestamp=1)),
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/37.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='af', color="light", className="m-1",n_clicks_timestamp=1)),
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/38.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='ag', color="light", className="m-1",n_clicks_timestamp=1)),
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/39.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='ah', color="light", className="m-1",n_clicks_timestamp=1)),
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/4.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='ai', color="light", className="m-1",n_clicks_timestamp=1)),
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/40.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='aj', color="light", className="m-1",n_clicks_timestamp=1)),
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/41.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='ak', color="light", className="m-1",n_clicks_timestamp=1)),
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/42.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='al', color="light", className="m-1",n_clicks_timestamp=1)),
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/43.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='am', color="light", className="m-1",n_clicks_timestamp=1)),
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/44.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='an', color="light", className="m-1",n_clicks_timestamp=1)),
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/45.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='ao', color="light", className="m-1",n_clicks_timestamp=1)),
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/46.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='ap', color="light", className="m-1",n_clicks_timestamp=1)),
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/47.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='aq', color="light", className="m-1",n_clicks_timestamp=1)),
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/48.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='ar', color="light", className="m-1",n_clicks_timestamp=1)),
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/49.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='ass', color="light", className="m-1",n_clicks_timestamp=1)),
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/5.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='at', color="light", className="m-1",n_clicks_timestamp=1)),
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/50.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='au', color="light", className="m-1",n_clicks_timestamp=1)),
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/51.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='av', color="light", className="m-1",n_clicks_timestamp=1)),
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/53.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='ba', color="light", className="m-1",n_clicks_timestamp=1)),
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/54.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='bb', color="light", className="m-1",n_clicks_timestamp=1)),
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/56.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='bd', color="light", className="m-1",n_clicks_timestamp=1)),
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/6.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='aw', color="light", className="m-1",n_clicks_timestamp=1)),
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/7.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='ax', color="light", className="m-1",n_clicks_timestamp=1)),
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/8.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='ay', color="light", className="m-1",n_clicks_timestamp=1)),
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/9.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='az', color="light", className="m-1",n_clicks_timestamp=1)),
		dbc.Col(
			dbc.Button(html.Img(src='https://github.com/niharika412/product_recommendations/blob/master/images/99.jpeg?raw=true', style={'height':'7rem', 'width':'7rem',"bottom": 2}),id='zz', color="light", className="m-1",n_clicks_timestamp=1))
		], style={'background-color':'#2d545e'})
    ],
    style=TOP_STYLE,
)

#Designing the bottom content

content = html.Div(
	[
	dbc.Row(
	[
	dbc.Col(html.P("Sim Score:")),
	dbc.Col(html.P("Sim Score:")),
	dbc.Col(html.P("Sim Score:")),
	dbc.Col(html.P("Sim Score:")),
	dbc.Col(html.P("Sim Score:")),
	
	], style={'background-color':'#e1b382'}),
	dbc.Row(
	[
	dbc.Col(html.Div(id='score1')),
	dbc.Col(html.Div(id='score2')),
	dbc.Col(html.Div(id='score3')),
	dbc.Col(html.Div(id='score4')),
	dbc.Col(html.Div(id='score5')),
	
	], style={'background-color':'#e1b382'}),
	dbc.Row(
	[
	dbc.Col(html.Img(id='output1', style={'height':'7rem', 'width':'7rem',"bottom": 2})),
	dbc.Col(html.Img(id='output2', style={'height':'7rem', 'width':'7rem',"bottom": 2})),
	dbc.Col(html.Img(id='output3', style={'height':'7rem', 'width':'7rem',"bottom": 2})),
	dbc.Col(html.Img(id='output4', style={'height':'7rem', 'width':'7rem',"bottom": 2})),
	dbc.Col(html.Img(id='output5', style={'height':'7rem', 'width':'7rem',"bottom": 2}))
	], style={'background-color':'#e1b382'})

],id="page-content", style=CONTENT_STYLE)

#linking and getting the top and bottom all together

app.layout = html.Div([dcc.Location(id="url"), top, content])

#Callbacks for the inputs and outputs. There are 10 outputs and 56 inputs. Input can vary and be large but for the limitations of the processor only 56 images are stored here.


@app.callback(
	[dash.dependencies.Output("output1", "src"),dash.dependencies.Output("output2", "src"),dash.dependencies.Output("output3", "src"),dash.dependencies.Output("output4", "src"),dash.dependencies.Output("output5", "src"),dash.dependencies.Output("score1", "children"),dash.dependencies.Output("score2", "children"),dash.dependencies.Output("score3", "children"),dash.dependencies.Output("score4", "children"),dash.dependencies.Output("score5", "children")], 
	[dash.dependencies.Input("a", "n_clicks_timestamp"),dash.dependencies.Input("b", "n_clicks_timestamp"),dash.dependencies.Input("c", "n_clicks_timestamp"),dash.dependencies.Input("d", "n_clicks_timestamp"),dash.dependencies.Input("e", "n_clicks_timestamp"),dash.dependencies.Input("f", "n_clicks_timestamp"),dash.dependencies.Input("g", "n_clicks_timestamp"),dash.dependencies.Input("h", "n_clicks_timestamp"),dash.dependencies.Input("i", "n_clicks_timestamp"),dash.dependencies.Input("j", "n_clicks_timestamp"),dash.dependencies.Input("k", "n_clicks_timestamp"),dash.dependencies.Input("l", "n_clicks_timestamp"),dash.dependencies.Input("m", "n_clicks_timestamp"),dash.dependencies.Input("n", "n_clicks_timestamp"),dash.dependencies.Input("o", "n_clicks_timestamp"),dash.dependencies.Input("p", "n_clicks_timestamp"),dash.dependencies.Input("q", "n_clicks_timestamp"),dash.dependencies.Input("r", "n_clicks_timestamp"),dash.dependencies.Input("s", "n_clicks_timestamp"),dash.dependencies.Input("t", "n_clicks_timestamp"),dash.dependencies.Input("u", "n_clicks_timestamp"),dash.dependencies.Input("v", "n_clicks_timestamp"),dash.dependencies.Input("w", "n_clicks_timestamp"),dash.dependencies.Input("x", "n_clicks_timestamp"),dash.dependencies.Input("y", "n_clicks_timestamp"),dash.dependencies.Input("z", "n_clicks_timestamp"),dash.dependencies.Input("aa", "n_clicks_timestamp"),dash.dependencies.Input("ab", "n_clicks_timestamp"),dash.dependencies.Input("ac", "n_clicks_timestamp"),dash.dependencies.Input("ad", "n_clicks_timestamp"),dash.dependencies.Input("ae", "n_clicks_timestamp"),dash.dependencies.Input("af", "n_clicks_timestamp"),dash.dependencies.Input("ag", "n_clicks_timestamp"),dash.dependencies.Input("ah", "n_clicks_timestamp"),dash.dependencies.Input("ai", "n_clicks_timestamp"),dash.dependencies.Input("aj", "n_clicks_timestamp"),dash.dependencies.Input("ak", "n_clicks_timestamp"),dash.dependencies.Input("al", "n_clicks_timestamp"),dash.dependencies.Input("am", "n_clicks_timestamp"),dash.dependencies.Input("an", "n_clicks_timestamp"),dash.dependencies.Input("ao", "n_clicks_timestamp"),dash.dependencies.Input("ap", "n_clicks_timestamp"),dash.dependencies.Input("aq", "n_clicks_timestamp"),dash.dependencies.Input("ar", "n_clicks_timestamp"),dash.dependencies.Input("ass", "n_clicks_timestamp"),dash.dependencies.Input("at", "n_clicks_timestamp"),dash.dependencies.Input("au", "n_clicks_timestamp"),dash.dependencies.Input("av", "n_clicks_timestamp"),dash.dependencies.Input("ba", "n_clicks_timestamp"),dash.dependencies.Input("bb", "n_clicks_timestamp"),dash.dependencies.Input("bd", "n_clicks_timestamp"),dash.dependencies.Input("aw", "n_clicks_timestamp"),dash.dependencies.Input("ax", "n_clicks_timestamp"),dash.dependencies.Input("ay", "n_clicks_timestamp"),dash.dependencies.Input("az", "n_clicks_timestamp"),dash.dependencies.Input("zz", "n_clicks_timestamp")]
)

#function for clicking of the image buttons
def click(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa,ab,ac,ad,ae,af,ag,ah,ai,aj,ak,al,am,an,ao,ap,aq,ar,ass,at,au,av,ba,bb,bd,aw,ax,ay,az,zz):
	l=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa,ab,ac,ad,ae,af,ag,ah,ai,aj,ak,al,am,an,ao,ap,aq,ar,ass,at,au,av,ba,bb,bd,aw,ax,ay,az,zz]
	l=list(map(int,l))
	m=max(l)
	ind=l.index(m)
	t=rect.retrieve_most_similar_products(files[ind])
	return t[0],t[1],t[2],t[3],t[4],t[5],t[6],t[7],t[8],t[9]

if __name__ == "__main__":
    app.run_server()