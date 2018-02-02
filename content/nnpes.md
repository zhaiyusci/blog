Title: Neuron-Network Pontential Energy Surfaces
Date: 2016-02-14 23:10
Category: Science
Authors: Yu Zhai

<p>Last year I read something about Neuron-Network Potential Energy Surface (NNPES) and I think it is worth learning.
Here are my notes.</p>
<p>One recommended paper one should read is <a href="http://dx.doi.org/10.1039/c1cp21668f">PCCP, 13, 17930 (2011)</a> by Joerg Behler.</p>
<p>Here I do not want to introduce the detail of the idea, because paper above give a nice definition.  NNPES do be a clever ider for it ignore the difficult physics in the problem.  Instead, it use a pure mathematical way to fit the pointwise energies (here we call it 'training').</p>
<p>Some guys argue that this methods just give a NNPES without a deeply conprehension of the model.  That is true.  However, this method give an effective way to let scientific guys to run MD or MC.  Somehow it is like <em>ab initio</em> way if one take the electronic methods as black box.</p>
<p>It should be kept in mind that in all NNPES is not that suitable for the high accuracy.  One can read <a href="http://dx.doi.org/10.1063/1.4904546">Dong H Zhang and his co-workers' work</a> to see how they got an accurate result with the help of spline.  I once tried one PES fitting using NN of the system of tri-boron (thanks to D.-Z. Yang), you can find that the NN works, but does not work accurately.  </p>
    
