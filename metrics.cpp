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

double percentile_90(std::vector<double>& v) {
    sort(v.begin(), v.end());

    return floor(0.90 * (v.size() + 1));
}

double percentile_99(std::vector<double>& v){

    sort(v.begin(), v.end());

    return floor(0.99 * (v.size() + 1));
}

double IQR(std::vector<double>& v){ 
    return floor(0.75 * (v.size() + 1)) - floor(0.25 * (v.size() + 1);
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

    std::cout << "90th percentile: " << percentile_99(v) << std::endl;
    
    std::cout << "99th percentile: " << percentile_99(v) << std::endl;

    std::cout << "Inter Quartile Range: " << IQR(v) << std::endl;
    
    return 0;
}
