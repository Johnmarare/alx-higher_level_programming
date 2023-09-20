#!/usr/bin/node

exports.converter = function (base) {
  // helper function to perform conversion recursively
  const convertRecurse = (number, base) =>
    number < base
      ? number.toString()
      : convertRecurse(Math.floor(number / base), base) + (number % base);

  // return the conveter function
  return (number) => convertRecurse(number, base);
};
