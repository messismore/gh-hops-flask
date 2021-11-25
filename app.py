from os import name
from flask import Flask
import ghhops_server as hs
from ghhops_server.component import HopsComponent
import rhino3dm

app = Flask(__name__)
hops = hs.Hops(app)

@hops.component(
    "/pointat",
    name="PointAt",
    description="Get point along a curve",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to evaluate"),
        hs.HopsNumber("t", "t", "Parameter on curve to evaluate", default=2.0)
    ],
    outputs=[hs.HopsPoint("P", "P", "Point on curve at t")]
)
def point_at(curve:rhino3dm.Curve, t):
    return curve.PointAt(t)

if __name__ == "__main__":
    app.run()