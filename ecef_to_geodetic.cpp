#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <cmath>

namespace py = pybind11;

// WGS84 ellipsoid constants
constexpr double a = 6378137.0;  // Semi-major axis (meters)
constexpr double f = 1 / 298.257223563;  // Flattening
constexpr double e2 = 2 * f - f * f;  // Eccentricity squared

std::tuple<double, double, double> ecef_to_geodetic(double x, double y, double z) {
    double lon = std::atan2(y, x);
    double p = std::sqrt(x * x + y * y);
    double lat = std::atan2(z, p * (1 - e2));
    double N, alt;
    
    for (int i = 0; i < 7; ++i) {  // Increased iterations for better precision
        N = a / std::sqrt(1 - e2 * std::sin(lat) * std::sin(lat));
        alt = p / std::cos(lat) - N;
        lat = std::atan2(z, p * (1 - e2 * (N / (N + alt))));
    }
    
    return {lat * 180.0 / M_PI, lon * 180.0 / M_PI, alt};
}

PYBIND11_MODULE(ecef_to_geodetic, m) {
    m.def("convert", &ecef_to_geodetic, "Convert ECEF (x, y, z) to geodetic (lat, lon, altitude)");
}
