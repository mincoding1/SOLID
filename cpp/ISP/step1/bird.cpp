#pragma once
#define interface struct

interface Bird {
    virtual void Fly() = 0;
    virtual void Molt() = 0;
};
