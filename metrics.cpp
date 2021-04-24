#include<iostream>
#include<algorithm>
#include<vector>
#include<numeric>
#include<cmath>

template<typename T>
double mean(std::vector<T>& v){
    const double sum = std::accumulate(v.begin(), v.end(), 0.0);
    return sum / v.size();
}

double median(std::vector<double>& v) {
    sort(v.begin(), v.end());

    if (v.size() % 2 != 0)
        return v[v.size()/2 - 1];
    else
        return (v[v.size()/2 - 1] + v[v.size()/2])/2; 
}

double variance(std::vector<double>& v){
    const double m = mean(v);
    double variance = 0.0;

    /* 
        Finding the variance:
        Var(v) = sum(
            (x_i - mean(v))^2
        )
        where, 0 <= i <= v.size()
    */
    std::for_each(v.begin(), v.end(), [&](const double x) { 
        variance += pow((x - m), 2);  
    });

    return variance / v.size();
}

double std_deviation(std::vector<double>& v) {

    // Standard deviation is just sqrt(Var(v))
    return std::sqrt(variance(v));
}

double mean_absolute_deviation(std::vector<double>& v) {
    const double m = median(v);

    std::vector<double> var;
    /* 
        Finding the variance:
        Var(v) = median(|x_i - median(v)|)
        where, 0 <= i <= v.size()
    */
    std::for_each(v.begin(), v.end(), [&](const double x) { 
        var.push_back(abs(x - m));  
    });

    // mean absolute deviation is just median(var)
    return median(var);
}

double nth_percentile_linear(std::vector<double>& v, int n){

    /*
        This is percentile found using `linear` interpolation

        More about it: https://en.wikipedia.org/wiki/Percentile#Second_variant,_%7F'%22%60UNIQ--postMath-0000004A-QINU%60%22'%7F 

        v.sort()

        x = ((n/100) * (v.size() - 1)) + 1 

        i_p = floor(x)
        d_p = x % 1 (or x - v2)

        The equation is:
            v_p = v[i_p] + d_p * (v[i_p + 1] - v2[i_p])
    */

    sort(v.begin(), v.end());

    double x = (n/100.0) * (v.size() - 1) + 1;

    int int_part = floor(x);
    double decimal_part = x - int_part;

    return v[int_part - 1] + decimal_part * ( v[int_part] - v[int_part -1 ]);
}

double IQR(std::vector<double>& v){ 
    return nth_percentile_linear(v, 75) - nth_percentile_linear(v, 25);
}


int main(int argc, char const *argv[])
{
    std::vector<double> v = {1, 2, 3, 4, 5, 6};

    std::vector<int> v1 = {1, 2, 3, 4, 5, 6};

    std::cout << v1.size() << std::endl;

    std::cout << "mean: " << mean<int>(v1) << std::endl;

    std::cout << "variance: " << variance(v) << std::endl;

    std::cout << "std deviation: " << std_deviation(v) << std::endl;

    std::cout << "median: " << median(v) << std::endl;

    std::cout << "mean absolute deviation: " << mean_absolute_deviation(v) << std::endl;

    std::cout << "90 th percentile: " << nth_percentile_linear(v, 90) << std::endl;
    
    std::cout << "99 th percentile: " << nth_percentile_linear(v, 99) << std::endl;

    std::cout << "Inter Quartile Range: " << IQR(v) << std::endl;

    return 0;
}
