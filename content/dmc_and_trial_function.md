Title: Diffusion Monte Carlo Methods and Trial Function
Date: 2016-08-21 14:40
Category: Science
Authors: Yu Zhai

For complex quantum system, the variation method is no longer useful for tho solve the problem precisely, you need a basis set of quite a large size.  *Quantum simulation* is used in such system.  *Monte Carlo Method* is widely used.

Recently I began to learn about these methods.  Notice that I say 'these' because methods can be called 'Quantum Monte Carlo' are more than three ones. 

Diffusion Monte Carlo is a, well, good idea.  I recommend [Rev. Mod. Phys. 73, 33 (2001)](http://dx.doi.org/10.1103/RevModPhys.73.33) as a reference.  

The problem is that if you use *mixed estimator* to get the energy, something terrible happened.   Just assume that the trial function is the eigenfunction of the ground state, which means actually we have got the right answer.  No matter whether your simulation converges to the walkers' distribution or not, the energy mixed estimator will give the answer -- the eigenvalue of ground state.  Similarly, if the trial function is the eigenfunction of the first excited state, the estimator will give the answer of first excited state, the reason is that the 'local energy' is relate to the trial function.  

Now let us simply do the superposition, to get the wave function for the superposition state of ground state and first excited state (just ignore the re-normalization).  Of course, the simulation answer shall be a value between the ground state energy and first excited state energy.

I have coded the Diffusion Monte Carlo method and test it on the harmonic oscillator system.  It is true: the mixed estimator is highly dependent on the trial function.  Watch out!
