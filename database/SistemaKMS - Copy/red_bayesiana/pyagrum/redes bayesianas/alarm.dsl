net Unnamed
{
	node KINKEDTUBE
	{
		TYPE = CPT;
		HEADER =
		{
			ID = KINKEDTUBE;
			NAME = "KINKEDTUBE";
		};
		PARENTS = ();
		DEFINITION =
		{
			NAMESTATES = (TRUE, FALSE);
			PROBABILITIES = (0.04, 0.96);
		};
	};

	node HYPOVOLEMIA
	{
		TYPE = CPT;
		HEADER =
		{
			ID = HYPOVOLEMIA;
			NAME = "HYPOVOLEMIA";
		};
		PARENTS = ();
		DEFINITION =
		{
			NAMESTATES = (TRUE, FALSE);
			PROBABILITIES = (0.2, 0.8);
		};
	};

	node INTUBATION
	{
		TYPE = CPT;
		HEADER =
		{
			ID = INTUBATION;
			NAME = "INTUBATION";
		};
		PARENTS = ();
		DEFINITION =
		{
			NAMESTATES = (NORMAL, ESOPHAGEAL, ONESIDED);
			PROBABILITIES = (0.92, 0.03, 0.05);
		};
	};

	node MINVOLSET
	{
		TYPE = CPT;
		HEADER =
		{
			ID = MINVOLSET;
			NAME = "MINVOLSET";
		};
		PARENTS = ();
		DEFINITION =
		{
			NAMESTATES = (LOW, NORMAL, HIGH);
			PROBABILITIES = (0.05, 0.9, 0.05);
		};
	};

	node PULMEMBOLUS
	{
		TYPE = CPT;
		HEADER =
		{
			ID = PULMEMBOLUS;
			NAME = "PULMEMBOLUS";
		};
		PARENTS = ();
		DEFINITION =
		{
			NAMESTATES = (TRUE, FALSE);
			PROBABILITIES = (0.01, 0.99);
		};
	};

	node INSUFFANESTH
	{
		TYPE = CPT;
		HEADER =
		{
			ID = INSUFFANESTH;
			NAME = "INSUFFANESTH";
		};
		PARENTS = ();
		DEFINITION =
		{
			NAMESTATES = (TRUE, FALSE);
			PROBABILITIES = (0.1, 0.9);
		};
	};

	node ERRLOWOUTPUT
	{
		TYPE = CPT;
		HEADER =
		{
			ID = ERRLOWOUTPUT;
			NAME = "ERRLOWOUTPUT";
		};
		PARENTS = ();
		DEFINITION =
		{
			NAMESTATES = (TRUE, FALSE);
			PROBABILITIES = (0.05, 0.95);
		};
	};

	node ERRCAUTER
	{
		TYPE = CPT;
		HEADER =
		{
			ID = ERRCAUTER;
			NAME = "ERRCAUTER";
		};
		PARENTS = ();
		DEFINITION =
		{
			NAMESTATES = (TRUE, FALSE);
			PROBABILITIES = (0.1, 0.9);
		};
	};

	node FIO2
	{
		TYPE = CPT;
		HEADER =
		{
			ID = FIO2;
			NAME = "FIO2";
		};
		PARENTS = ();
		DEFINITION =
		{
			NAMESTATES = (LOW, NORMAL);
			PROBABILITIES = (0.05, 0.95);
		};
	};

	node LVFAILURE
	{
		TYPE = CPT;
		HEADER =
		{
			ID = LVFAILURE;
			NAME = "LVFAILURE";
		};
		PARENTS = ();
		DEFINITION =
		{
			NAMESTATES = (TRUE, FALSE);
			PROBABILITIES = (0.05, 0.95);
		};
	};

	node DISCONNECT
	{
		TYPE = CPT;
		HEADER =
		{
			ID = DISCONNECT;
			NAME = "DISCONNECT";
		};
		PARENTS = ();
		DEFINITION =
		{
			NAMESTATES = (TRUE, FALSE);
			PROBABILITIES = (0.1, 0.9);
		};
	};

	node ANAPHYLAXIS
	{
		TYPE = CPT;
		HEADER =
		{
			ID = ANAPHYLAXIS;
			NAME = "ANAPHYLAXIS";
		};
		PARENTS = ();
		DEFINITION =
		{
			NAMESTATES = (TRUE, FALSE);
			PROBABILITIES = (0.01, 0.99);
		};
	};

	node PAP
	{
		TYPE = CPT;
		HEADER =
		{
			ID = PAP;
			NAME = "PAP";
		};
		PARENTS = (PULMEMBOLUS);
		DEFINITION =
		{
			NAMESTATES = (LOW, NORMAL, HIGH);
			PROBABILITIES = (0.01, 0.19, 0.8, 0.05, 0.9, 0.05);
		};
	};

	node STROKEVOLUME
	{
		TYPE = CPT;
		HEADER =
		{
			ID = STROKEVOLUME;
			NAME = "STROKEVOLUME";
		};
		PARENTS = (LVFAILURE, HYPOVOLEMIA);
		DEFINITION =
		{
			NAMESTATES = (LOW, NORMAL, HIGH);
			PROBABILITIES = (0.98, 0.01, 0.01, 0.5, 0.49, 0.01, 0.95, 0.04, 0.01, 0.05, 0.9, 0.05);
		};
	};

	node TPR
	{
		TYPE = CPT;
		HEADER =
		{
			ID = TPR;
			NAME = "TPR";
		};
		PARENTS = (ANAPHYLAXIS);
		DEFINITION =
		{
			NAMESTATES = (LOW, NORMAL, HIGH);
			PROBABILITIES = (0.98, 0.01, 0.01, 0.3, 0.4, 0.3);
		};
	};

	node LVEDVOLUME
	{
		TYPE = CPT;
		HEADER =
		{
			ID = LVEDVOLUME;
			NAME = "LVEDVOLUME";
		};
		PARENTS = (HYPOVOLEMIA, LVFAILURE);
		DEFINITION =
		{
			NAMESTATES = (LOW, NORMAL, HIGH);
			PROBABILITIES = (0.95, 0.04, 0.01, 0.01, 0.09, 0.9, 0.98, 0.01, 0.01, 0.05, 0.9, 0.05);
		};
	};

	node VENTMACH
	{
		TYPE = CPT;
		HEADER =
		{
			ID = VENTMACH;
			NAME = "VENTMACH";
		};
		PARENTS = (MINVOLSET);
		DEFINITION =
		{
			NAMESTATES = (ZERO, LOW, NORMAL, HIGH);
			PROBABILITIES = (0.05, 0.93, 0.01, 0.01, 0.05, 0.01, 0.93, 0.01, 0.05, 0.01, 0.01, 0.93);
		};
	};

	node PCWP
	{
		TYPE = CPT;
		HEADER =
		{
			ID = PCWP;
			NAME = "PCWP";
		};
		PARENTS = (LVEDVOLUME);
		DEFINITION =
		{
			NAMESTATES = (LOW, NORMAL, HIGH);
			PROBABILITIES = (0.95, 0.04, 0.01, 0.04, 0.95, 0.01, 0.01, 0.04, 0.95);
		};
	};

	node SHUNT
	{
		TYPE = CPT;
		HEADER =
		{
			ID = SHUNT;
			NAME = "SHUNT";
		};
		PARENTS = (INTUBATION, PULMEMBOLUS);
		DEFINITION =
		{
			NAMESTATES = (NORMAL, HIGH);
			PROBABILITIES = (0.1, 0.9, 0.95, 0.05, 0.1, 0.9, 0.95, 0.05, 0.01, 0.99, 0.05, 0.95);
		};
	};

	node HISTORY
	{
		TYPE = CPT;
		HEADER =
		{
			ID = HISTORY;
			NAME = "HISTORY";
		};
		PARENTS = (LVFAILURE);
		DEFINITION =
		{
			NAMESTATES = (TRUE, FALSE);
			PROBABILITIES = (0.9, 0.1, 0.01, 0.99);
		};
	};

	node VENTTUBE
	{
		TYPE = CPT;
		HEADER =
		{
			ID = VENTTUBE;
			NAME = "VENTTUBE";
		};
		PARENTS = (DISCONNECT, VENTMACH);
		DEFINITION =
		{
			NAMESTATES = (ZERO, LOW, NORMAL, HIGH);
			PROBABILITIES = (0.97, 0.01, 0.01, 0.01, 0.97, 0.01, 0.01, 0.01, 0.97, 0.01, 0.01, 0.01, 0.01, 0.01, 0.97, 0.01, 0.97, 0.01, 0.01, 0.01, 0.97, 0.01, 0.01, 0.01, 0.01, 0.97, 0.01, 0.01, 0.01, 0.01, 0.01, 0.97);
		};
	};

	node CVP
	{
		TYPE = CPT;
		HEADER =
		{
			ID = CVP;
			NAME = "CVP";
		};
		PARENTS = (LVEDVOLUME);
		DEFINITION =
		{
			NAMESTATES = (LOW, NORMAL, HIGH);
			PROBABILITIES = (0.95, 0.04, 0.01, 0.04, 0.95, 0.01, 0.01, 0.29, 0.7);
		};
	};

	node VENTLUNG
	{
		TYPE = CPT;
		HEADER =
		{
			ID = VENTLUNG;
			NAME = "VENTLUNG";
		};
		PARENTS = (VENTTUBE, KINKEDTUBE, INTUBATION);
		DEFINITION =
		{
			NAMESTATES = (ZERO, LOW, NORMAL, HIGH);
			PROBABILITIES = (0.97, 0.01, 0.01, 0.01, 0.97, 0.01, 0.01, 0.01, 0.97, 0.01, 0.01, 0.01, 0.97, 0.01, 0.01, 0.01, 0.3, 0.68, 0.01, 0.01, 0.95, 0.03, 0.01, 0.01, 0.01, 0.01, 0.01, 0.97, 0.01, 0.97, 0.01, 0.01, 0.95, 0.03, 0.01, 0.01, 0.97, 0.01, 0.01, 0.01, 0.01, 0.97, 0.01, 0.01, 0.97, 0.01, 0.01, 0.01, 0.97, 0.01, 0.01, 0.01, 0.5, 0.48, 0.01, 0.01, 0.97, 0.01, 0.01, 0.01, 0.01, 0.01, 0.97, 0.01, 0.4, 0.58, 0.01, 0.01, 0.97, 0.01, 0.01, 0.01, 0.01, 0.01, 0.97, 0.01, 0.97, 0.01, 0.01, 0.01, 0.97, 0.01, 0.01, 0.01, 0.3, 0.68, 0.01, 0.01, 0.97, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.97);
		};
	};

	node MINVOL
	{
		TYPE = CPT;
		HEADER =
		{
			ID = MINVOL;
			NAME = "MINVOL";
		};
		PARENTS = (VENTLUNG, INTUBATION);
		DEFINITION =
		{
			NAMESTATES = (ZERO, LOW, NORMAL, HIGH);
			PROBABILITIES = (0.97, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.97, 0.5, 0.48, 0.01, 0.01, 0.01, 0.97, 0.01, 0.01, 0.01, 0.97, 0.01, 0.01, 0.97, 0.01, 0.01, 0.01, 0.5, 0.48, 0.01, 0.01, 0.01, 0.01, 0.97, 0.01, 0.01, 0.01, 0.97, 0.01, 0.6, 0.38, 0.01, 0.01, 0.97, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.97);
		};
	};

	node PRESS
	{
		TYPE = CPT;
		HEADER =
		{
			ID = PRESS;
			NAME = "PRESS";
		};
		PARENTS = (VENTTUBE, KINKEDTUBE, INTUBATION);
		DEFINITION =
		{
			NAMESTATES = (ZERO, LOW, NORMAL, HIGH);
			PROBABILITIES = (0.97, 0.01, 0.01, 0.01, 0.05, 0.25, 0.25, 0.45, 0.97, 0.01, 0.01, 0.01, 0.2, 0.75, 0.04, 0.01, 0.01, 0.01, 0.01, 0.97, 0.01, 0.29, 0.3, 0.4, 0.01, 0.01, 0.01, 0.97, 0.01, 0.9, 0.08, 0.01, 0.01, 0.3, 0.49, 0.2, 0.01, 0.15, 0.25, 0.59, 0.01, 0.97, 0.01, 0.01, 0.2, 0.7, 0.09, 0.01, 0.97, 0.01, 0.01, 0.01, 0.01, 0.01, 0.08, 0.9, 0.97, 0.01, 0.01, 0.01, 0.01, 0.01, 0.38, 0.6, 0.01, 0.01, 0.08, 0.9, 0.97, 0.01, 0.01, 0.01, 0.01, 0.01, 0.97, 0.01, 0.97, 0.01, 0.01, 0.01, 0.1, 0.84, 0.05, 0.01, 0.01, 0.01, 0.01, 0.97, 0.4, 0.58, 0.01, 0.01, 0.01, 0.01, 0.01, 0.97);
		};
	};

	node VENTALV
	{
		TYPE = CPT;
		HEADER =
		{
			ID = VENTALV;
			NAME = "VENTALV";
		};
		PARENTS = (VENTLUNG, INTUBATION);
		DEFINITION =
		{
			NAMESTATES = (ZERO, LOW, NORMAL, HIGH);
			PROBABILITIES = (0.97, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.97, 0.01, 0.01, 0.97, 0.01, 0.03, 0.95, 0.01, 0.01, 0.01, 0.97, 0.01, 0.01, 0.97, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.97, 0.01, 0.94, 0.04, 0.01, 0.01, 0.01, 0.97, 0.01, 0.01, 0.97, 0.01, 0.01, 0.97, 0.01, 0.01, 0.01, 0.01, 0.88, 0.1, 0.01);
		};
	};

	node ARTCO2
	{
		TYPE = CPT;
		HEADER =
		{
			ID = ARTCO2;
			NAME = "ARTCO2";
		};
		PARENTS = (VENTALV);
		DEFINITION =
		{
			NAMESTATES = (LOW, NORMAL, HIGH);
			PROBABILITIES = (0.01, 0.01, 0.98, 0.01, 0.01, 0.98, 0.04, 0.92, 0.04, 0.9, 0.09, 0.01);
		};
	};

	node PVSAT
	{
		TYPE = CPT;
		HEADER =
		{
			ID = PVSAT;
			NAME = "PVSAT";
		};
		PARENTS = (VENTALV, FIO2);
		DEFINITION =
		{
			NAMESTATES = (LOW, NORMAL, HIGH);
			PROBABILITIES = (1, 0, 0, 0.95, 0.04, 0.01, 1, 0, 0, 0.01, 0.95, 0.04, 0.99, 0.01, 0, 0.95, 0.04, 0.01, 0.95, 0.04, 0.01, 0.01, 0.01, 0.98);
		};
	};

	node SAO2
	{
		TYPE = CPT;
		HEADER =
		{
			ID = SAO2;
			NAME = "SAO2";
		};
		PARENTS = (SHUNT, PVSAT);
		DEFINITION =
		{
			NAMESTATES = (LOW, NORMAL, HIGH);
			PROBABILITIES = (0.98, 0.01, 0.01, 0.98, 0.01, 0.01, 0.01, 0.98, 0.01, 0.98, 0.01, 0.01, 0.01, 0.01, 0.98, 0.69, 0.3, 0.01);
		};
	};

	node EXPCO2
	{
		TYPE = CPT;
		HEADER =
		{
			ID = EXPCO2;
			NAME = "EXPCO2";
		};
		PARENTS = (ARTCO2, VENTLUNG);
		DEFINITION =
		{
			NAMESTATES = (ZERO, LOW, NORMAL, HIGH);
			PROBABILITIES = (0.97, 0.01, 0.01, 0.01, 0.01, 0.97, 0.01, 0.01, 0.01, 0.01, 0.97, 0.01, 0.01, 0.01, 0.01, 0.97, 0.01, 0.97, 0.01, 0.01, 0.97, 0.01, 0.01, 0.01, 0.01, 0.01, 0.97, 0.01, 0.01, 0.01, 0.01, 0.97, 0.01, 0.97, 0.01, 0.01, 0.01, 0.01, 0.97, 0.01, 0.97, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.97);
		};
	};

	node CATECHOL
	{
		TYPE = CPT;
		HEADER =
		{
			ID = CATECHOL;
			NAME = "CATECHOL";
		};
		PARENTS = (TPR, ARTCO2, SAO2, INSUFFANESTH);
		DEFINITION =
		{
			NAMESTATES = (NORMAL, HIGH);
			PROBABILITIES = (0.01, 0.99, 0.01, 0.99, 0.7, 0.3, 0.01, 0.99, 0.05, 0.95, 0.7, 0.3, 0.01, 0.99, 0.05, 0.95, 0.95, 0.05, 0.01, 0.99, 0.05, 0.95, 0.7, 0.3, 0.01, 0.99, 0.05, 0.95, 0.95, 0.05, 0.05, 0.95, 0.05, 0.95, 0.95, 0.05, 0.01, 0.99, 0.01, 0.99, 0.7, 0.3, 0.01, 0.99, 0.05, 0.95, 0.7, 0.3, 0.01, 0.99, 0.05, 0.95, 0.99, 0.01, 0.01, 0.99, 0.05, 0.95, 0.7, 0.3, 0.01, 0.99, 0.05, 0.95, 0.99, 0.01, 0.05, 0.95, 0.05, 0.95, 0.99, 0.01, 0.01, 0.99, 0.01, 0.99, 0.1, 0.9, 0.01, 0.99, 0.01, 0.99, 0.1, 0.9, 0.01, 0.99, 0.01, 0.99, 0.3, 0.7, 0.01, 0.99, 0.01, 0.99, 0.1, 0.9, 0.01, 0.99, 0.01, 0.99, 0.3, 0.7, 0.01, 0.99, 0.01, 0.99, 0.3, 0.7);
		};
	};

	node HR
	{
		TYPE = CPT;
		HEADER =
		{
			ID = HR;
			NAME = "HR";
		};
		PARENTS = (CATECHOL);
		DEFINITION =
		{
			NAMESTATES = (LOW, NORMAL, HIGH);
			PROBABILITIES = (0.05, 0.9, 0.05, 0.01, 0.09, 0.9);
		};
	};

	node HRBP
	{
		TYPE = CPT;
		HEADER =
		{
			ID = HRBP;
			NAME = "HRBP";
		};
		PARENTS = (ERRLOWOUTPUT, HR);
		DEFINITION =
		{
			NAMESTATES = (LOW, NORMAL, HIGH);
			PROBABILITIES = (0.98, 0.01, 0.01, 0.3, 0.4, 0.3, 0.01, 0.98, 0.01, 0.4, 0.59, 0.01, 0.98, 0.01, 0.01, 0.01, 0.01, 0.98);
		};
	};

	node HRSAT
	{
		TYPE = CPT;
		HEADER =
		{
			ID = HRSAT;
			NAME = "HRSAT";
		};
		PARENTS = (ERRCAUTER, HR);
		DEFINITION =
		{
			NAMESTATES = (LOW, NORMAL, HIGH);
			PROBABILITIES = (0.333333, 0.333333, 0.333333, 0.333333, 0.333333, 0.333333, 0.01, 0.98, 0.01, 0.333333, 0.333333, 0.333333, 0.98, 0.01, 0.01, 0.01, 0.01, 0.98);
		};
	};

	node CO
	{
		TYPE = CPT;
		HEADER =
		{
			ID = CO;
			NAME = "CO";
		};
		PARENTS = (HR, STROKEVOLUME);
		DEFINITION =
		{
			NAMESTATES = (LOW, NORMAL, HIGH);
			PROBABILITIES = (0.98, 0.01, 0.01, 0.95, 0.04, 0.01, 0.3, 0.69, 0.01, 0.95, 0.04, 0.01, 0.04, 0.95, 0.01, 0.01, 0.3, 0.69, 0.8, 0.19, 0.01, 0.01, 0.04, 0.95, 0.01, 0.01, 0.98);
		};
	};

	node HREKG
	{
		TYPE = CPT;
		HEADER =
		{
			ID = HREKG;
			NAME = "HREKG";
		};
		PARENTS = (HR, ERRCAUTER);
		DEFINITION =
		{
			NAMESTATES = (LOW, NORMAL, HIGH);
			PROBABILITIES = (0.333333, 0.333333, 0.333333, 0.333333, 0.333333, 0.333333, 0.01, 0.98, 0.01, 0.333333, 0.333333, 0.333333, 0.98, 0.01, 0.01, 0.01, 0.01, 0.98);
		};
	};

	node BP
	{
		TYPE = CPT;
		HEADER =
		{
			ID = BP;
			NAME = "BP";
		};
		PARENTS = (TPR, CO);
		DEFINITION =
		{
			NAMESTATES = (LOW, NORMAL, HIGH);
			PROBABILITIES = (0.98, 0.01, 0.01, 0.98, 0.01, 0.01, 0.3, 0.6, 0.1, 0.98, 0.01, 0.01, 0.1, 0.85, 0.05, 0.05, 0.4, 0.55, 0.9, 0.09, 0.01, 0.05, 0.2, 0.75, 0.01, 0.09, 0.9);
		};
	};

};