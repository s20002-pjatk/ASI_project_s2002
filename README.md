# ASI_project_s2002
# Table of contents
## 1. [General](#general)
## 2. [Architecture](#architecture)
## 3. [Instruction](#instruction)
## 4. [Authors](#authors)

## 1. General <a name="general"></a>
The application was designed to support choice of wine. It can help non-expert customers to select quqlity wine. It can be a part of bigger software as well as stand-alone application. Besides, the pipeline should also work in a loop that: 
creates ML model, 
eveluates the model using new batches of data
detectcts data drift
in case of the data drift retraines and updates the model

Data to construct machine learning model were downlowaded from Kaggle.

## 2. Architecture <a name="architecture"></a>
The architecture of the application is described by the diagram shown in the Figure 1.

<mxfile host="app.diagrams.net" modified="2022-07-01T19:07:23.507Z" agent="5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36" etag="AEuVXiZAkNEgmVo-lWya" version="20.0.4" type="github">
  <diagram id="TBJxufM5Nzm1yPSdCavO" name="Page-1">
    <mxGraphModel dx="4142" dy="1164" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="0" pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="lPiTISsA9HOT361Q44LX-1" value="" style="whiteSpace=wrap;html=1;aspect=fixed;rounded=1;" vertex="1" parent="1">
          <mxGeometry x="-570" y="320" width="220" height="220" as="geometry" />
        </mxCell>
        <mxCell id="lPiTISsA9HOT361Q44LX-7" value="Data preparation" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;" vertex="1" parent="1">
          <mxGeometry x="-520" y="320" width="130" height="30" as="geometry" />
        </mxCell>
        <mxCell id="lPiTISsA9HOT361Q44LX-8" value="&lt;br&gt;" style="whiteSpace=wrap;html=1;aspect=fixed;rounded=1;" vertex="1" parent="1">
          <mxGeometry x="-50" y="330" width="220" height="220" as="geometry" />
        </mxCell>
        <mxCell id="lPiTISsA9HOT361Q44LX-9" value="Construction of the model" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;" vertex="1" parent="1">
          <mxGeometry x="-10" y="340" width="130" height="30" as="geometry" />
        </mxCell>
        <mxCell id="lPiTISsA9HOT361Q44LX-10" value="&lt;br&gt;" style="whiteSpace=wrap;html=1;aspect=fixed;rounded=1;" vertex="1" parent="1">
          <mxGeometry x="750" y="330" width="220" height="220" as="geometry" />
        </mxCell>
        <mxCell id="lPiTISsA9HOT361Q44LX-11" value="Monitoring" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;" vertex="1" parent="1">
          <mxGeometry x="790" y="340" width="130" height="30" as="geometry" />
        </mxCell>
        <mxCell id="lPiTISsA9HOT361Q44LX-15" value="initial&amp;nbsp;&lt;br&gt;data" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="-910" y="430" width="120" height="60" as="geometry" />
        </mxCell>
        <mxCell id="lPiTISsA9HOT361Q44LX-17" value="data transformation" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="-520" y="380" width="120" height="60" as="geometry" />
        </mxCell>
        <mxCell id="lPiTISsA9HOT361Q44LX-19" value="deduplication" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="-520" y="460" width="120" height="60" as="geometry" />
        </mxCell>
        <mxCell id="lPiTISsA9HOT361Q44LX-23" value="" style="endArrow=classic;html=1;rounded=0;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="-350" y="435" as="sourcePoint" />
            <mxPoint x="-260" y="435" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="lPiTISsA9HOT361Q44LX-24" value="curated dataset.csv" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="-260" y="410" width="120" height="60" as="geometry" />
        </mxCell>
        <mxCell id="lPiTISsA9HOT361Q44LX-25" value="" style="endArrow=classic;html=1;rounded=0;entryX=-0.005;entryY=0.586;entryDx=0;entryDy=0;entryPerimeter=0;" edge="1" parent="1" target="lPiTISsA9HOT361Q44LX-1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="-790" y="449.5" as="sourcePoint" />
            <mxPoint x="-700" y="449.5" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="lPiTISsA9HOT361Q44LX-27" value="" style="endArrow=classic;html=1;rounded=0;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="-140" y="440" as="sourcePoint" />
            <mxPoint x="-50" y="440" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="lPiTISsA9HOT361Q44LX-28" value="dataset split" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="-5" y="390" width="120" height="40" as="geometry" />
        </mxCell>
        <mxCell id="lPiTISsA9HOT361Q44LX-29" value="choice of the top performing algorithm" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry y="440" width="120" height="40" as="geometry" />
        </mxCell>
        <mxCell id="lPiTISsA9HOT361Q44LX-30" value="fine-tuning of the top performing algorithm" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry y="490" width="120" height="40" as="geometry" />
        </mxCell>
        <mxCell id="lPiTISsA9HOT361Q44LX-31" value="" style="endArrow=classic;html=1;rounded=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;" edge="1" parent="1" source="lPiTISsA9HOT361Q44LX-38" target="lPiTISsA9HOT361Q44LX-10">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="400" y="440" as="sourcePoint" />
            <mxPoint x="260" y="440" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="lPiTISsA9HOT361Q44LX-32" value="new&amp;nbsp;&lt;br&gt;batch" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="-920" y="325" width="120" height="60" as="geometry" />
        </mxCell>
        <mxCell id="lPiTISsA9HOT361Q44LX-33" value="" style="endArrow=classic;html=1;rounded=0;entryX=0.005;entryY=0.159;entryDx=0;entryDy=0;entryPerimeter=0;" edge="1" parent="1" target="lPiTISsA9HOT361Q44LX-1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="-800" y="355.08" as="sourcePoint" />
            <mxPoint x="-581.0999999999999" y="354.50000000000006" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="lPiTISsA9HOT361Q44LX-34" value="" style="endArrow=classic;html=1;rounded=0;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="-350" y="354.5999999999999" as="sourcePoint" />
            <mxPoint x="-250" y="355" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="lPiTISsA9HOT361Q44LX-35" value="curated&lt;br&gt;batch.csv" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="-250" y="325" width="120" height="60" as="geometry" />
        </mxCell>
        <mxCell id="lPiTISsA9HOT361Q44LX-36" value="" style="endArrow=classic;html=1;rounded=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;" edge="1" parent="1" source="lPiTISsA9HOT361Q44LX-35">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="-130" y="279.9999999999999" as="sourcePoint" />
            <mxPoint x="440" y="440" as="targetPoint" />
            <Array as="points">
              <mxPoint x="-70" y="355" />
              <mxPoint x="-70" y="260" />
              <mxPoint x="440" y="260" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="lPiTISsA9HOT361Q44LX-38" value="model.pkl" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="260" y="410" width="120" height="60" as="geometry" />
        </mxCell>
        <mxCell id="lPiTISsA9HOT361Q44LX-39" value="" style="endArrow=classic;html=1;rounded=0;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="170" y="440" as="sourcePoint" />
            <mxPoint x="260" y="440" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="lPiTISsA9HOT361Q44LX-40" value="Drift detected" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;rounded=1;" vertex="1" parent="1">
          <mxGeometry x="820" y="750" width="80" height="80" as="geometry" />
        </mxCell>
        <mxCell id="lPiTISsA9HOT361Q44LX-42" value="" style="endArrow=classic;html=1;rounded=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" target="lPiTISsA9HOT361Q44LX-40">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="860" y="700" as="sourcePoint" />
            <mxPoint x="1080" y="660.4" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="lPiTISsA9HOT361Q44LX-43" value="" style="endArrow=classic;html=1;rounded=0;exitX=0;exitY=0.5;exitDx=0;exitDy=0;" edge="1" parent="1" source="lPiTISsA9HOT361Q44LX-40">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="640" y="809.5" as="sourcePoint" />
            <mxPoint x="540" y="790" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="lPiTISsA9HOT361Q44LX-44" value="data evaluation" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="790" y="385" width="120" height="40" as="geometry" />
        </mxCell>
        <mxCell id="lPiTISsA9HOT361Q44LX-46" value="&lt;br&gt;" style="whiteSpace=wrap;html=1;aspect=fixed;rounded=1;" vertex="1" parent="1">
          <mxGeometry x="310" y="745" width="220" height="220" as="geometry" />
        </mxCell>
        <mxCell id="lPiTISsA9HOT361Q44LX-47" value="Merging data" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;" vertex="1" parent="1">
          <mxGeometry x="365" y="770" width="130" height="30" as="geometry" />
        </mxCell>
        <mxCell id="lPiTISsA9HOT361Q44LX-48" value="merging initial data with new batches" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="360" y="820" width="120" height="70" as="geometry" />
        </mxCell>
        <mxCell id="lPiTISsA9HOT361Q44LX-51" value="" style="endArrow=classic;html=1;rounded=0;exitX=0.5;exitY=1;exitDx=0;exitDy=0;" edge="1" parent="1" source="lPiTISsA9HOT361Q44LX-15">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="-850" y="570" as="sourcePoint" />
            <mxPoint x="640" y="790" as="targetPoint" />
            <Array as="points">
              <mxPoint x="-850" y="980" />
              <mxPoint x="640" y="980" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="lPiTISsA9HOT361Q44LX-52" value="data evaluation" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="800" y="570" width="120" height="60" as="geometry" />
        </mxCell>
        <mxCell id="lPiTISsA9HOT361Q44LX-53" value="drift detection" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="800" y="650" width="120" height="60" as="geometry" />
        </mxCell>
        <mxCell id="lPiTISsA9HOT361Q44LX-54" value="" style="endArrow=none;html=1;rounded=0;entryX=0.5;entryY=1;entryDx=0;entryDy=0;exitX=0.5;exitY=0;exitDx=0;exitDy=0;" edge="1" parent="1" source="lPiTISsA9HOT361Q44LX-52" target="lPiTISsA9HOT361Q44LX-10">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="220" y="610" as="sourcePoint" />
            <mxPoint x="270" y="560" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="lPiTISsA9HOT361Q44LX-56" value="" style="endArrow=none;html=1;rounded=0;exitX=0.5;exitY=0;exitDx=0;exitDy=0;" edge="1" parent="1" source="lPiTISsA9HOT361Q44LX-53" target="lPiTISsA9HOT361Q44LX-52">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="870" y="580" as="sourcePoint" />
            <mxPoint x="860" y="640" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="lPiTISsA9HOT361Q44LX-57" value="drift detection" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="790" y="450" width="120" height="60" as="geometry" />
        </mxCell>
        <mxCell id="lPiTISsA9HOT361Q44LX-58" value="" style="endArrow=classic;html=1;rounded=0;exitX=0.5;exitY=0;exitDx=0;exitDy=0;" edge="1" parent="1" source="lPiTISsA9HOT361Q44LX-35">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="220" y="610" as="sourcePoint" />
            <mxPoint x="690" y="790" as="targetPoint" />
            <Array as="points">
              <mxPoint x="-190" y="200" />
              <mxPoint x="1000" y="200" />
              <mxPoint x="1000" y="870" />
              <mxPoint x="840" y="870" />
              <mxPoint x="690" y="870" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="lPiTISsA9HOT361Q44LX-59" value="retraining the model" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry y="570" width="120" height="60" as="geometry" />
        </mxCell>
        <mxCell id="lPiTISsA9HOT361Q44LX-60" value="" style="endArrow=classic;html=1;rounded=0;entryX=0.5;entryY=1;entryDx=0;entryDy=0;exitX=0;exitY=0.5;exitDx=0;exitDy=0;" edge="1" parent="1" source="lPiTISsA9HOT361Q44LX-62" target="lPiTISsA9HOT361Q44LX-59">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="280" y="660" as="sourcePoint" />
            <mxPoint x="270" y="560" as="targetPoint" />
            <Array as="points">
              <mxPoint x="210" y="660" />
              <mxPoint x="60" y="660" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="lPiTISsA9HOT361Q44LX-61" value="" style="endArrow=classic;html=1;rounded=0;exitX=0.5;exitY=0;exitDx=0;exitDy=0;entryX=0.5;entryY=1;entryDx=0;entryDy=0;" edge="1" parent="1" source="lPiTISsA9HOT361Q44LX-59" target="lPiTISsA9HOT361Q44LX-8">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="220" y="610" as="sourcePoint" />
            <mxPoint x="430" y="440" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="lPiTISsA9HOT361Q44LX-62" value="larger dataset.csv" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="360" y="630" width="120" height="60" as="geometry" />
        </mxCell>
        <mxCell id="lPiTISsA9HOT361Q44LX-64" value="" style="endArrow=classic;html=1;rounded=0;entryX=0.5;entryY=1;entryDx=0;entryDy=0;" edge="1" parent="1" source="lPiTISsA9HOT361Q44LX-46" target="lPiTISsA9HOT361Q44LX-62">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="220" y="610" as="sourcePoint" />
            <mxPoint x="270" y="560" as="targetPoint" />
          </mxGeometry>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>

## 3.Installation <a name="installation"></a>

The easiest way to run the application is to use Anaconda Navigator. It can be download from: https://anaconda.org/ 

After installation of the anaconda software, create a new virtual evironment in Anaconda Navigator. Recommended python version is 3.8.13.

To activate new environmet , type in the fllowing command in Anaconda Prompt:

(base) C:\Users\saras>conda activate ASI

Neccessary libraries to run the application were listed below:
- numpy 
- pandas
- pycaret

They can be installed in the new virtual environement by typing in the Anaconda Prompt the following command:

(ASI) C:\Users\saras> pip install name_of_the_library

To run the application type in  Anaconda Prompt the following command:
(ASI) C:\Users\saras> python wine_classifier_mod2.py

Make sure that Anaconda Prompt points the correct location where the file is stored. 


## 5. Authors <a name="authors"></a>
Sara Szymkuć is the only author of the application.
