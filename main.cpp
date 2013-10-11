#include "QuakeLibOkada.h"
#include <iostream>
#include <stdio.h>

//bool custom_isnan(double);
//double fRand(double,double);

int main() {

	double pie = 3.1415926;

	double _C 	= 1000.0;
	double _L 	= 10000.0;
	double _W 	= 10000.0;
	double _UT	= 0.0;
	double _US	= 5.0;
	double _UD	= 0.0;
	double _DIP	= pie/2.0;
	double _X	= 10000.0;
	double _Y	= 5000.0;
	double _LAMBDA = 1.0;
	double _MU     = 1.0;

	//cout << "\n\nInput the fault geometry::::";
	//cout << "\nFault depth [m]: ";
	//cin  >> _C;
	//cout << "Fault length [m]: ";
	//cin  >> _L;
	//cout << "Fault width [m]:";
	//cin  >> _W;
	//cout << "Fault angle [rad]:";
	//cin  >> _DIP;
	//cout << "Strike slip [m]:";
	//cin  >> _US;
	//cout << "Dip slip [m]:";
	//cin  >> _UD;
	//cout << "Tensile slip [m]:";
	//cin  >> _UT;

	//cout << "\nWhere do you to evaluate the change in gravity?";
	//cout << "\nX [m]\t:";
	//cin  >> _X;
	//cout << "Y [m]\t:";
	//cin  >> _Y;

    quakelib::Okada     O;
    double DG           	  = O.dg(_X,_Y,_C,_DIP,_L,_W,_US,_UD,_UT,_LAMBDA,_MU);
    quakelib::Vec<3> loc;
    loc[0]=_X;
    loc[1]=_Y;
    loc[2]=0.0;

    quakelib::Vec<3> DISPLACE;
    DISPLACE = O.calc_displacement_vector(loc,_C,_DIP,_L,_W,_US,_UD,_UT,_LAMBDA,_MU);

    double DZ = DISPLACE[2];

    std::cout.precision(3);
    std::cout << std::scientific;
    std::cout << "\nx:\t\t" << "y:\t\t" << "dz:\t\t" << "dg:";
    std::cout << "\n" << _X << "\t" << _Y << "\t" << DZ << "\t" << DG << "\n\n";

    return 0;
}



/*
//==-=-=-=-----------------------------------

int main() {
    using namespace quakelib;
    //want to test simply if I can compile a simple script that uses the
    //   new QuakeLibOkada methods, trying to get some numbers out just
    //   to see that it at least is some sort of function, verification
    //   to come later.

    double Xmin = -5000;
    double Xmax = 15000;
    double Ymin = -10000;
    double Ymax = 10000;

    quakelib::Vec<3> Cs;
    Cs[0] = 500;
    Cs[1] = 1000;
    Cs[2] = 10000;

    quakelib::Vec<3> Ls;
    Ls[0] = 1000;
    Ls[1] = 10000;
    Ls[2] = 100000;

    quakelib::Vec<3> Ws;
    Ws[0] = 1000;
    Ws[1] = 10000;
    Ws[2] = 100000;

    quakelib::Vec<3> slips;
    slips[0] = 5;
    slips[1] = 20;
    slips[2] = 100;

    quakelib::Vec<3> dips;
    dips[0] = 3.1415926/10.0;
    dips[1] = 3.1415926/4.0;
    dips[2] = 3.1415926/2.0;

    int i;
    int l;
    int k;
    int j;
    int m;
    int x;
    int y;
    double z;
    int Nxmax = 50;
    int Nymax = 50;

    //std::cout.precision(3);
    //std::cout << "\ntolerance " << TOLERANCE;
    std::cout << "\n\nx:\t\t" << "y:\t\t" << "dz:\t\t"  << "dg:\n";
    //std::cout << std::scientific;
    std::cout << std::fixed;

    double op_counter   = 0.0;
    double notuseful_count = 0.0;

    for (k=0;k<3;k++) {
        for (j=0;j<3;j++) {
            for (i=0;i<3;i++) {
                for (l=0;l<3;l++) {
                    for (m=0;m<3;m++) {

                        double c        = Cs[k];
                        double L        = Ls[j];
                        double W        = Ws[i];
                        double slip     = slips[m];
                        double dip_rad  = dips[l];
                        double dip_deg  = dip_rad*180.0/3.1415926;

                        //std::cout << "\nc  " << c;
                        //std::cout << "\tL " << L;
                        //std::cout << "\tW " << W;
                        //std::cout << "\tdip " << dip_deg;
                        //std::cout << "\tslip " << slip;

                        std::cout.precision(3);
                        std::cout << std::scientific;

                        for (int x=0;x<Nxmax;x++){
                            for (int y=0;y<Nymax;y++){
                                op_counter++;
                                double seed = (5*x+3*y)*(7*x+y);
                                srand (seed);

                                double xloc = fRand(Xmin,Xmax);
                                double yloc = fRand(Ymin,Ymax);

                                double _US = 0.0;
                                double _UD = 0.0;
                                double _UT = slip;

                                quakelib::Okada     O;
                                double DG           = O.dg(xloc,yloc,c,L,W,_US,_UD,_UT);
                                double DZ           = O.uz(xloc,yloc,0.0,c,L,W,_US,_UD,_UT);

                                //std::cout << "\n" << xloc << "\t" << yloc << "\t" << DZ << "\t" << DG;

                                //bool yes_zero = (fabs(DG) < pow(10,-100)) || (fabs(DZ) < pow(10,-100));
                                //bool yes_nan  = custom_isnan(DG) || custom_isnan(DZ);

                                //if (yes_zero || yes_nan) {
                                //    notuseful_count++;
                                //}
                                if ( (fabs(DG) < pow(10,-100)) || custom_isnan(DG)) {
                                    notuseful_count++;
                                    //std::cout << "*";
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    double percent_bad = 100*notuseful_count/op_counter;
    std::cout.precision(1);
    std::cout << std::fixed;
    std::cout << "\n" << op_counter << " ops, " << percent_bad << "percent bad\n\n";


    double c = Cs[0];
    double L = Ls[0];
    double W = Ws[0];
    double dip_rad = dips[0];
    double slip    = slips[0];

    for (int x=0;x<xmax;x++){
        for (int y=0;y<ymax;y++){
            double xloc         = x*pow(3,x)*pow(-1.0,y);
            double yloc         = y*pow(3,y)*pow(-1.0,y+1);
            quakelib::Okada     O;
            double DG           = O.dg(xloc,yloc,c,L,W,slip*cos(dip_rad),slip*sin(dip_rad),slip);
            double DZ           = O.uz(xloc,yloc,0.0,c,L,W,slip*cos(dip_rad),slip*sin(dip_rad),slip);

            std::cout << "\nisnan? " << custom_isnan(DG) << " shown here " << DG;
        }
    }
    
    return 1;
}

*/
