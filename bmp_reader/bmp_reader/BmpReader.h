#pragma once

#include <fstream>

/*14 bytes:
Signature2
Size4
Reserved2
Reserved2
Offset4*/
struct BmpHeader {
	unsigned size;
	unsigned offset;
	unsigned short signature;
	unsigned short reserved1;
	unsigned short reserved2;

	friend std::ifstream operator>>(std::ifstream&, BmpHeader&);
};


struct BmpInfo {

};

class BmpReader {
public:
	BmpReader();
	~BmpReader();
private:
	char* path_;
	BmpHeader header_;
	BmpInfo info_;
};