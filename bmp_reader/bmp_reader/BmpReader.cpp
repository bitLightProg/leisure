#include "BmpReader.h"

std::ifstream operator>>(std::ifstream &fin, BmpHeader &header) {
	fin.read(reinterpret_cast<char*>(&header.signature), 2);
	fin.read(reinterpret_cast<char*>(&header.size), 4);
	fin.read(reinterpret_cast<char*>(&header.reserved1), 2);
	fin.read(reinterpret_cast<char*>(&header.reserved2), 2);
	fin.read(reinterpret_cast<char*>(&header.offset), 4);
}


BmpReader::BmpReader() {
}


BmpReader::~BmpReader() {
}
