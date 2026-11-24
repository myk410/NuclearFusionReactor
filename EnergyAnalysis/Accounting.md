# Whole-facility energy accounting — E001

## Boundaries and definitions
Use a plant gate electrical meter over a stated time horizon T (seconds). Net exported energy must be positive over an operating and major-maintenance cycle. Report site electricity separately from embodied replacement/manufacturing energy; use an expanded lifecycle ledger where that data exists. This distinction prevents an operational result from implying a lifecycle result. No fuel-delivered gain is a substitute for this meter.

P_f is fusion reaction power (MW); P_h is external heat or drive reaching the explicitly defined fuel/target boundary; Q=P_f/P_h. Laser-to-target and actual fuel-deposited boundaries differ: label Q_target and Q_fuel separately. eta_d=P_h/P_driver,e is electrical-to-boundary driver efficiency, dimensionless. P_a covers **all other on-state** electric loads, excluding driver input already counted: refrigeration, pumping, controls, fuel cycle, injection/target manufacture on-site, exhaust and waste treatment. If current drive is included in P_h, do not add it again to P_a.

Let c be captured fraction of fusion energy; M be an optional blanket nuclear energy multiplier relative to fusion energy deposited (baseline M=1). M>1 requires a separately justified nuclear-reaction ledger; it is not free energy or an adjustable thermal-efficiency factor. Let r be the fraction of P_h recovered as heat in the same conversion cycle. Let eta_t be effective gross heat-to-electric efficiency, bounded by the heat-source/sink temperatures and actual cycle losses. All these efficiencies are dimensionless. Different thermal grades require separate streams; a single eta_t is only a reduction model.

For thermal conversion only:

P_g = eta_t (c M P_f + r P_h)

P_net,on = P_g - P_h/eta_d - P_a

With a=P_a/P_f and x=P_net,on/P_f:

x = eta_t(c M + r/Q) - 1/(eta_d Q) - a.             (1)

If eta_t c M > a and (1/eta_d - eta_t r)>0,

Q_min = (1/eta_d - eta_t r)/(eta_t c M - a).         (2)

Equality is electrical breakeven, not a useful engineering margin. If eta_t c M <= a, no finite Q can close this simplified balance. Check algebra against direct power accounting and dimensions. For r=0, eta_d=1, c=M=1, a=0, Q_min=1/eta_t; as eta_d→0, Q_min→infinity.

Direct conversion extension: partition P_f into mutually exclusive streams f_j, sum f_j<=1. Then P_g=sum_j eta_j c_j f_j P_f + recovered external-drive contributions. A directly collected particle cannot also contribute its full original energy to the thermal stream. Only its residual energy may be recovered. D–T neutron energy is not directly collected by an electrostatic charged-particle converter. Alpha energy extracted before thermalization may reduce self-heating and Q; these variables cannot be improved independently without proof.

Average over duty fraction d with off-state load P_off and N starts:

E_net/T = d P_net,on - (1-d)P_off - N E_start/T - E_maint/T.  (3)

Here energies are MW·s (MJ), times seconds. E_start excludes any startup consumption already integrated into on/off loads. Storage and grid-conditioning losses need their own terms. Annual availability includes failures and remote maintenance, not merely pulse duty. A positive on-state balance can have negative cycle-average balance.

## Worked scenario — illustrative inputs, not measured plant parameters
P_f=1000 MW, Q=10, eta_d=0.5, eta_t=0.4, c=0.95, M=1, r=0, a=0.08.
P_h=100 MW; driver input=200 MWe; gross=380 MWe; auxiliary=80 MWe; net on=100 MWe. Equation (2) gives Q_min=6.6667. For d=0.70 and P_off=20 MWe with no added startup/maintenance energy, mean net=64 MWe. None of these assumptions establish a buildable reactor.

## Source boundary
Framework is a project derivation consistent with the plant-level distinction in R004. Numeric ranges in the model are analyst-selected stress tests, **not** fits to R004 or any machine. Validate assumptions against architecture-specific engineering data before application. No whole-facility dataset was available for calibration in this pass.
