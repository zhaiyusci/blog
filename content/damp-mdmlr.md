Title: Damping function in Morse/Long-Range Potential Energy Model 
Date: 2016-03-12 22:20
Category: Science
Authors: Yu Zhai

<p>It is a great success that the application of Morse/Long-Range (MLR) in van der Waals (vdW) complex.  MLR is devloped by R. J. Le Roy et al..  You may want to use it when building you own bi-atomic system model.  That's cool and you can always use <a href="http://scienide2.uwaterloo.ca/~rleroy/betaFIT/">betaFIT</a>, where you can get the code and manual.</p>
<p>In the past, MLR had difficulty in <em>short range</em> (as its name, it focused on <em>long range</em>).  It means that you can use a inverse power model to represent the long range behaviour of a system, like when the two monomers in the complex distants away by 10 Angstrom or more.  But in long range, the coefficients of the inverse power terms tend to be 0 for the electrons there merge together.</p>
<p>Luckily, Prof Le Roy came up with the damping function (Yeppy!) which can fit this decrease when the nuclear distance vanishes.  If you wanna get the details, please read <a href="http://www.tandfonline.com/doi/abs/10.1080/00268976.2010.527304#.VuQoRSbAPtQ">Mol. Phys., 109, 435 (2011)</a>.  By the way, this modified damping function has already been included in the newest version of betaFIT.</p>
<p>Recently.</p>
<p>Acctually today, I enhanced the MLR in Multi Dimension system by adding a Modified Tang-Tonnies damping function with the paramenter in it as a function of angles.  By this way, I have managed the fitting error one the third of the previous model.  I will going to talk about this topic in this years ISMS in UIUC.</p>
  
