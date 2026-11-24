# M002 — what one enhanced-rate measurement can identify

For a reduced illustrative yield law Y_i=A_i n exp(k_i u), n is an unknown target-density normalization; u is a dimensionless screening parameter; k_i is a known dimensionless sensitivity; A_i includes exposure, geometry and cross-section normalization. Poisson expected counts are N_i. The information matrix for theta=(log n,u) is a sum of outer products N_i (1,k_i)^T(1,k_i). Its determinant is zero with one independent sensitivity, so no unique density/screening attribution is possible without additional information. With two slopes it is N1 N2(k1-k2)².

This mathematical example does not assert that screening follows a simple exponential over all energies or that k is known in Thunderbird. Real stopping, depth-dependent density, backgrounds, ion composition and efficiency need additional parameters. It demonstrates an identifiability requirement, not a new nuclear effect.

For two equal-duration independent Poisson measurements with ratio 1+delta, baseline expected count N, a rough difference statistic is z≈delta sqrt[N/(2+delta)]. Rearrangement gives N≈z²(2+delta)/delta²; adding a normal power term provides an approximate planning sensitivity. The code executes these calculations for delta=.15, but these counts do not validate or reinterpret the reported 15(2)% uncertainty. No experimental acquisition protocol is provided.

See ComputationalModels/inference_and_tradeoffs.py and Simulations/InferenceAndTradeoffs.json for actual executed values and checks.
