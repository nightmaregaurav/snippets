// a class that will remove the precision issue of number in javascript
// by using string to store the number and using the string to
// do the calculation by using the basic methods of digit by digit calculation.

function ParseLargeNumber(value: number | string): LargeNumber {
    return new LargeNumber(value);
}

class LargeNumber {
    private readonly value: string;
    private _isNegative: boolean;
    get isNegative(): boolean {
        return this._isNegative;
    }
    private set isNegative(value: boolean) {
        this._isNegative = value;
    }

    constructor(value: number | string) {
        if (typeof value === 'number') {
            this.value = value.toString();
        } else {
            if (!/^-?\d*(\.\d+)?$/.test(value) && value !== '-') {
                throw new Error('Invalid number: ' + value);
            }
            this.value = value;
        }
        this._isNegative = this.value[0] === '-';
        if (this._isNegative) {
            this.value = this.value.slice(1);
        }

        this.value = this.value.replace(/^0+/, '');
        if (this.value[0] === '.') {
            this.value = '0' + this.value;
        }

        if (!this.value.includes('.')) {
            this.value += '.0';
        }

        if (this.value.split('.')[1].replace(/0/g, '') === '') {
            this.value = this.value.split('.')[0] + '.0';
        }
    }

    /**
     *
     * @returns The string representation of the LargeNumber instance
     *
     */
    public toString(): string {
        return (this.isNegative ? '-' : '') + this.value;
    }

    /**
     *
     * @returns Wither the LargeNumber instance is a decimal number or not
     *
     */
    public hasDecimalPoint(): boolean {
        return this.value.split('.')[1] !== '0'
    }

    /**
     *
     * @returns The LargeNumber instance negated [negated means the sign of the number is changed]
     *
     */
    public negate(): LargeNumber {
        return LargeNumber.negate(this);
    }

    /**
     *
     *  @returns The LargeNumber instance with the absolute value of the current LargeNumber instance
     *
     */
    public abs(): LargeNumber {
        return LargeNumber.abs(this);
    }

    /**
     *
     * @param precision The number of decimal places to round the LargeNumber instance to
     * @returns The LargeNumber instance rounded to the specified precision
     *
     */
    public round(precision: number): LargeNumber {
        return LargeNumber.round(this, precision);
    }

    /**
     *
     * @param largeNumber The LargeNumber instance to compare with [The right operand]
     * @returns true if the current LargeNumber instance is less than the right operand
     *
     */
    public isLessThan(largeNumber: LargeNumber): boolean {
        return LargeNumber.lessThan(this, largeNumber);
    }

    /**
     *
     * @param largeNumber The LargeNumber instance to compare with [The right operand]
     * @returns true if the current LargeNumber instance is greater than the right operand
     *
     */
    public isGreaterThan(largeNumber: LargeNumber): boolean {
        return LargeNumber.greaterThan(this, largeNumber);
    }

    /**
     *
     * @param largeNumber The LargeNumber instance to compare with [The right operand]
     * @returns true if the current LargeNumber instance is equal to the right operand
     *
     */
    public equals(largeNumber: LargeNumber): boolean {
        return LargeNumber.equals(this, largeNumber);
    }

    /**
     *
     * @param largeNumber The LargeNumber instance to compare with [The right operand]
     * @returns true if the current LargeNumber instance is less than or equal to the right operand
     *
     */
    public isLessThanOrEqual(largeNumber: LargeNumber): boolean {
        return LargeNumber.lessThanOrEqual(this, largeNumber);
    }

    /**
     *
     * @param largeNumber The LargeNumber instance to compare with [The right operand]
     * @returns true if the current LargeNumber instance is greater than or equal to the right operand
     *
     */
    public isGreaterThanOrEqual(largeNumber: LargeNumber): boolean {
        return LargeNumber.greaterThanOrEqual(this, largeNumber);
    }

    /**
     *
     * @param params The LargeNumber instances to add to the current LargeNumber instance
     * @returns The LargeNumber instance that is the sum of the current LargeNumber instance and the right operands
     *
     */
    public add(...params: LargeNumber[]): LargeNumber {
        return params.reduce((acc, largeNumber) => LargeNumber.add(acc, largeNumber), this);
    }

    /**
     *
     * @param params The LargeNumber instances to subtract from the current LargeNumber instance
     * @returns The LargeNumber instance that is the difference of the current LargeNumber instance and the right operands
     *
     */
    public subtract(...params: LargeNumber[]): LargeNumber {
        return params.reduce((acc, largeNumber) => LargeNumber.subtract(acc, largeNumber), this);
    }

    /**
     *
     * @param params The LargeNumber instances to multiply with the current LargeNumber instance
     * @returns The LargeNumber instance that is the product of the current LargeNumber instance and the right operands
     *
     */
    public multiply(...params: LargeNumber[]): LargeNumber {
        return params.reduce((acc, largeNumber) => LargeNumber.multiply(acc, largeNumber), this);
    }

    /**
     *
     * @param divisor The LargeNumber instance to divide the current LargeNumber instance by
     * @returns The Array with the first element being the LargeNumber instance that is the quotient of the current LargeNumber instance and the right operand and the second element being the LargeNumber instance that is the remainder of the current LargeNumber instance and the right operand
     *
     */
    public quotientAndRemainder(divisor: LargeNumber): [LargeNumber, LargeNumber] {
        return LargeNumber.longDivisionWithRemainder(this, divisor);
    }

    /**
     *
     * @param divisor The LargeNumber instance to divide the current LargeNumber instance by
     * @returns The LargeNumber instance that is the quotient of the current LargeNumber instance and the right operand
     *
     */
    public quotient(divisor: LargeNumber): LargeNumber {
        return this.divide(divisor);
    }

    /**
     *
     * @param divisor The LargeNumber instance to divide the current LargeNumber instance by
     * @returns The LargeNumber instance that is the remainder of the current LargeNumber instance and the right operand
     *
     */
    public mod(divisor: LargeNumber): LargeNumber {
        return this.remainder(divisor);
    }

    /**
     *
     * @param divisor The LargeNumber instance to divide the current LargeNumber instance by
     * @returns The LargeNumber instance that is the remainder of the current LargeNumber instance and the right operand
     *
     */
    public remainder(divisor: LargeNumber): LargeNumber {
        return LargeNumber.remainder(this, divisor);
    }

    /**
     *
     * @param precision The number of decimal places to round the LargeNumber instance to
     * @param params The LargeNumber instances to divide the current LargeNumber instance by
     * @returns The LargeNumber instance that is the quotient of the current LargeNumber instance and the right operands with the specified precision for decimal places
     *
     */
    public divideWithPrecision(precision: number, ...params: LargeNumber[]): LargeNumber {
        return params.reduce((acc, largeNumber) => LargeNumber.divide(acc, largeNumber, precision), this);
    }

    /**
     *
     * @param params The LargeNumber instances to divide the current LargeNumber instance by
     * @returns The LargeNumber instance that is the quotient of the current LargeNumber instance and the right operands with a precision of 10 decimal places
     *
     */
    public divide(...params: LargeNumber[]): LargeNumber {
        return params.reduce((acc, largeNumber) => LargeNumber.divide(acc, largeNumber, 10), this);
    }

    /**
     *
     * @returns An array with the first element being the numerator and the second element being the denominator
     *
     */
    public asFraction(): [LargeNumber, LargeNumber] {
        return LargeNumber.decimalToFraction(this);
    }

    /**
     *
     * @param exponent The exponent number
     * @returns The LargeNumber instance that is the result of the current LargeNumber instance raised to the power of the exponent number
     *
     */
    public power(exponent: LargeNumber): LargeNumber {
        return LargeNumber.power(this, exponent);
    }

    /**
     *
     * @param root The root number
     * @returns The LargeNumber instance that is the result of the current LargeNumber instance raised to the power of 1/root number
     *
     */
    public root(root: LargeNumber): LargeNumber {
        return LargeNumber.root(this, root);
    }

    //// Static methods ////

    /**
     *
     * @param number1 The first number to compare
     * @param number2 The second number to compare
     * @returns The normalized numbers with 0 padding on the left of the numbers and on right after the decimal point to make the numbers have the same length
     * @private
     *
     */
    private static normalizeWith0Padding(number1: string, number2: string): [string, string] {
        const beforeDecimal1 = number1.split('.')[0];
        const beforeDecimal2 = number2.split('.')[0];
        const afterDecimal1 = number1.split('.')[1] || '';
        const afterDecimal2 = number2.split('.')[1] || '';

        const maxLengthBeforeDecimal = Math.max(beforeDecimal1.length, beforeDecimal2.length);
        const maxLengthAfterDecimal = Math.max(afterDecimal1.length, afterDecimal2.length);

        const paddedBeforeDecimal1 = beforeDecimal1.padStart(maxLengthBeforeDecimal, '0');
        const paddedBeforeDecimal2 = beforeDecimal2.padStart(maxLengthBeforeDecimal, '0');

        const paddedAfterDecimal1 = afterDecimal1.padEnd(maxLengthAfterDecimal, '0');
        const paddedAfterDecimal2 = afterDecimal2.padEnd(maxLengthAfterDecimal, '0');

        const paddedNumber1 = `${paddedBeforeDecimal1}.${paddedAfterDecimal1}`;
        const paddedNumber2 = `${paddedBeforeDecimal2}.${paddedAfterDecimal2}`;

        return [paddedNumber1, paddedNumber2];
    }

    /**
     *
     * @param number1 The first number to adjust
     * @param number2 The second number to adjust
     * @returns The adjusted numbers with no decimal point and with 0 padding on the right to make the numbers have the same length (same as multiplying the numbers by 10 to the power of the number of maximum decimal places)
     * @private
     *
     */
    private static adjustNumeralsToRemoveDecimalPoint(number1: string, number2: string): [string, string] {
        const decimalPlaces1 = number1.split('.')[1].length;
        const decimalPlaces2 = number2.split('.')[1].length;
        const decimalPlaces = Math.max(decimalPlaces1, decimalPlaces2);
        const adjustedNumber1 = number1.replace('.', '') + '0'.repeat(decimalPlaces - decimalPlaces1);
        const adjustedNumber2 = number2.replace('.', '') + '0'.repeat(decimalPlaces - decimalPlaces2);
        return [adjustedNumber1, adjustedNumber2];
    }

    /**
     *
     * @param largeNumber The LargeNumber instance to negate
     * @returns The LargeNumber instance negated [negated means the sign of the number is changed]
     * @private
     *
     */
    private static negate(largeNumber: LargeNumber): LargeNumber {
        largeNumber.isNegative = !largeNumber.isNegative;
        return largeNumber;
    }

    /**
     *
     * @param largeNumber The LargeNumber instance to get the absolute value of
     * @returns The LargeNumber instance with the absolute value of the current LargeNumber instance [absolute value means the sign of the number is removed]
     * @private
     *
     */
    private static abs(largeNumber: LargeNumber): LargeNumber {
        if (largeNumber.isNegative) {
            return ParseLargeNumber(largeNumber.value);
        }
        return largeNumber;
    }

    /**
     *
     * @param largeNumber The LargeNumber instance to round
     * @param precision The number of decimal places to round the LargeNumber instance to
     * @returns The LargeNumber instance rounded to the specified precision
     * @private
     *
     */
    private static round(largeNumber: LargeNumber, precision: number): LargeNumber {
        const numberAsDecimalString = largeNumber.value;
        const numberImmediatelyAfterPrecisionPosition = numberAsDecimalString.split('.')[1][precision] || '0';
        if (parseInt(numberImmediatelyAfterPrecisionPosition) < 5) {
            return ParseLargeNumber(
                numberAsDecimalString.split('.')[0]
                + '.'
                + numberAsDecimalString.split('.')[1].slice(0, precision)
            );
        }
        const numberAfterDecimal = ParseLargeNumber(numberAsDecimalString.split('.')[1].slice(0, precision)).add(ParseLargeNumber(1));
        const numberAfterDecimalAsString = numberAfterDecimal.value.split('.')[0];
        const isCarryOver = numberAfterDecimalAsString.length > precision;
        const numberBeforeDecimal = isCarryOver ? ParseLargeNumber(numberAsDecimalString.split('.')[0]).add(ParseLargeNumber(1)) : ParseLargeNumber(numberAsDecimalString.split('.')[0]);
        const numberBeforeDecimalAsString = numberBeforeDecimal.value.split('.')[0];
        const finalNumberAfterDecimal = isCarryOver ? numberAfterDecimalAsString.slice(1) : numberAfterDecimalAsString.padStart(precision, '0');
        return ParseLargeNumber(`${numberBeforeDecimalAsString}.${finalNumberAfterDecimal}`);
    }

    /**
     *
     * @param left The LargeNumber instance to compare with [The left operand]
     * @param right The LargeNumber instance to compare with [The right operand]
     * @returns true if the left operand is less than the right operand
     * @private
     *
     */
    private static lessThan(left: LargeNumber, right: LargeNumber): boolean {
        if (left.isNegative !== right.isNegative) {
            return left.isNegative;
        }
        const leftLengthWithoutDecimal = left.value.replace('.', '').length;
        const rightLengthWithoutDecimal = right.value.replace('.', '').length;
        if (leftLengthWithoutDecimal !== rightLengthWithoutDecimal) {
            return leftLengthWithoutDecimal < rightLengthWithoutDecimal;
        }
        const [leftNumber, rightNumber] = LargeNumber.normalizeWith0Padding(left.value, right.value);
        const result = leftNumber < rightNumber;
        if (left.isNegative) {
            return !result;
        }
        return result;
    }

    /**
     *
     * @param left The LargeNumber instance to compare with [The left operand]
     * @param right The LargeNumber instance to compare with [The right operand]
     * @returns true if the left operand is greater than the right operand
     * @private
     *
     */
    private static greaterThan(left: LargeNumber, right: LargeNumber): boolean {
        if (left.isNegative !== right.isNegative) {
            return !left.isNegative;
        }
        const leftLengthWithoutDecimal = left.value.replace('.', '').length;
        const rightLengthWithoutDecimal = right.value.replace('.', '').length;
        if (leftLengthWithoutDecimal !== rightLengthWithoutDecimal) {
            return leftLengthWithoutDecimal > rightLengthWithoutDecimal;
        }
        const [leftNumber, rightNumber] = LargeNumber.normalizeWith0Padding(left.value, right.value);
        const result = leftNumber > rightNumber;
        if (left.isNegative) {
            return !result;
        }
        return result;
    }

    /**
     *
     * @param left The LargeNumber instance to compare with [The left operand]
     * @param right The LargeNumber instance to compare with [The right operand]
     * @returns true if the left operand is equal to the right operand
     * @private
     *
     */
    private static equals(left: LargeNumber, right: LargeNumber): boolean {
        if (left.isNegative !== right.isNegative) {
            return false;
        }
        return left.value === right.value;
    }

    /**
     *
     * @param left The LargeNumber instance to compare with [The left operand]
     * @param right The LargeNumber instance to compare with [The right operand]
     * @returns true if the left operand is less than or equal to the right operand
     * @private
     *
     */
    private static lessThanOrEqual(left: LargeNumber, right: LargeNumber): boolean {
        return this.lessThan(left, right) || this.equals(left, right);
    }

    /**
     *
     * @param left The LargeNumber instance to compare with [The left operand]
     * @param right The LargeNumber instance to compare with [The right operand]
     * @returns true if the left operand is greater than or equal to the right operand
     * @private
     *
     */
    private static greaterThanOrEqual(left: LargeNumber, right: LargeNumber): boolean {
        return this.greaterThan(left, right) || this.equals(left, right);
    }

    /**
     *
     * @param left The LargeNumber instance to add to
     * @param right The LargeNumber instance to add
     * @returns The LargeNumber instance that is the sum of the left and right operands
     * @private
     *
     */
    private static add(left: LargeNumber, right: LargeNumber): LargeNumber {
        if (left.isNegative !== right.isNegative) {
            if (left.isNegative) {
                return right.subtract(left.abs());
            }
            return left.subtract(right.abs());
        }
        const isResultNegative = left.isNegative && right.isNegative;
        const [number1, number2] = LargeNumber.normalizeWith0Padding(left.value, right.value);
        let carry = 0;
        let result = '';
        for (let i = number1.length - 1; i >= 0; i--) {
            if (number1[i] === '.') {
                result = '.' + result;
                continue;
            }
            const digit1 = parseInt(number1[i], 10);
            const digit2 = parseInt(number2[i], 10);
            let sum = digit1 + digit2 + carry;
            if (sum >= 10) {
                carry = Math.floor(sum / 10);
                sum %= 10;
            } else {
                carry = 0;
            }
            result = sum.toString() + result;
        }
        if (carry > 0) {
            result = carry.toString() + result;
        }
        result = result.replace(/^0+/, '');
        return ParseLargeNumber((isResultNegative ? '-' : '') + result);
    }

    /**
     *
     * @param left The LargeNumber instance to subtract from
     * @param right The LargeNumber instance to subtract
     * @returns The LargeNumber instance that is the difference of the left and right operands
     * @private
     *
     */
    private static subtract(left: LargeNumber, right: LargeNumber): LargeNumber {
        if (left.isNegative && !right.isNegative) {
            return left.add(right.negate());
        }
        if (!left.isNegative && right.isNegative) {
            return left.add(right.abs());
        }
        if (left.isNegative && right.isNegative) {
            const temp = left;
            left = right;
            right = temp;
            left = left.abs();
            right = right.abs();
        }
        const isResultNegative = left.isLessThan(right);
        if (isResultNegative) {
            const temp = left;
            left = right;
            right = temp;
        }
        const [number1, number2] = LargeNumber.normalizeWith0Padding(left.value, right.value);
        let borrow = 0;
        let result = '';
        for (let i = number1.length - 1; i >= 0; i--) {
            if (number1[i] === '.') {
                result = '.' + result;
                continue;
            }
            const digit1 = parseInt(number1[i], 10);
            const digit2 = parseInt(number2[i], 10);
            let diff = digit1 - digit2 - borrow;
            if (diff < 0) {
                diff += 10;
                borrow = 1;
            } else {
                borrow = 0;
            }
            result = diff.toString() + result;
        }

        result = result.replace(/^0+/, '');
        return ParseLargeNumber((isResultNegative ? '-' : '') + result);
    }

    /**
     *
     * @param left The LargeNumber instance to multiply
     * @param right The LargeNumber instance to multiply
     * @returns The LargeNumber instance that is the product of the left and right operands
     * @private
     *
     */
    private static multiply(left: LargeNumber, right: LargeNumber): LargeNumber {
        let [leftAsString, rightAsString] = LargeNumber.normalizeWith0Padding(left.value, right.value);
        const resultDecimalPlaces = leftAsString.split('.')[1].length + rightAsString.split('.')[1].length;
        leftAsString = leftAsString.replace('.', '');
        rightAsString = rightAsString.replace('.', '');

        const isResultNegative = left.isNegative !== right.isNegative;

        const resultArray: number[] = [];
        for (let i = leftAsString.length - 1; i >= 0; i--) {
            for (let j = rightAsString.length - 1; j >= 0; j--) {
                const product = parseInt(leftAsString[i], 10) * parseInt(rightAsString[j], 10);
                const sum = product + resultArray[i + j + 1] || 0;
                resultArray[i + j] = (resultArray[i + j] || 0) + Math.floor(sum / 10);
                resultArray[i + j + 1] = sum % 10;
            }
        }

        let resultString = resultArray.join('').replace(/^0+/, '');
        if (resultString === '') {
            resultString = '0';
        }
        resultString = resultString.slice(0, resultString.length - resultDecimalPlaces) + '.' + resultString.slice(resultString.length - resultDecimalPlaces);

        return ParseLargeNumber((isResultNegative ? '-' : '') + resultString);
    }

    /**
     *
     * @param left The LargeNumber instance to divide
     * @param right The LargeNumber instance to divide by
     * @returns The Array with the first element being the LargeNumber instance that is the quotient of the left and right operands and the second element being the LargeNumber instance that is the remainder of the left and right operands. [Uses brute force division. IE. subtracting the divisor from the dividend until the dividend is less than the divisor]
     * @private
     *
     */
    private static bruteDivide(left: LargeNumber, right: LargeNumber): [LargeNumber, LargeNumber] {
        let quotient = ParseLargeNumber(0);
        let remainder = left;
        while (remainder.isGreaterThanOrEqual(right)) {
            remainder = remainder.subtract(right);
            quotient = quotient.add(ParseLargeNumber(1));
        }
        return [quotient, remainder];
    }

    /**
     *
     * @param left The LargeNumber instance to divide
     * @param right The LargeNumber instance to divide by
     * @returns The Array with the first element being the LargeNumber instance that is the quotient of the left and right operands and the second element being the LargeNumber instance that is the remainder of the left and right operands [This method division does not take sign of the numbers into account]
     * @private
     *
     */
    private static longDivisionWithRemainder(left: LargeNumber, right: LargeNumber): [LargeNumber, LargeNumber] {
        left = left.abs();
        right = right.abs();

        if (right.equals(ParseLargeNumber(0))) {
            throw new Error('Cannot divide by zero');
        }
        if (left.equals(ParseLargeNumber(0))) {
            return [ParseLargeNumber(0), ParseLargeNumber(0)];
        }
        if (right.equals(ParseLargeNumber(1))) {
            return [left, ParseLargeNumber(0)];
        }
        if (right.equals(left)) {
            return [ParseLargeNumber(1), ParseLargeNumber(0)];
        }
        if (right.isGreaterThan(left)) {
            return [ParseLargeNumber(0), left];
        }

        const [adjustedLeft, adjustedRight] = LargeNumber.adjustNumeralsToRemoveDecimalPoint(left.value, right.value);
        let quotient = "";
        let currentDividend = ""
        const divisor = ParseLargeNumber(adjustedRight);
        for (let i = 0; i < adjustedLeft.length; i++) {
            currentDividend += adjustedLeft[i];
            if (ParseLargeNumber(currentDividend).isGreaterThanOrEqual(divisor)) {
                const [currentQuotient, currentRemainder] = LargeNumber.bruteDivide(ParseLargeNumber(currentDividend), divisor);
                quotient = quotient + currentQuotient.value.split('.')[0];
                currentDividend = currentRemainder.value.split('.')[0];
            } else {
                quotient = quotient + '0';
            }
        }
        return [ParseLargeNumber(quotient), ParseLargeNumber(currentDividend)];
    }

    /**
     *
     * @param left The LargeNumber instance to divide
     * @param right The LargeNumber instance to divide by
     * @returns The LargeNumber instance that is the quotient of the left and right operands [Discards the remainder]
     * @private
     *
     */
    private static quotient(left: LargeNumber, right: LargeNumber): LargeNumber {
        return this.longDivisionWithRemainder(left, right)[0];
    }

    /**
     *
     * @param left The LargeNumber instance to divide
     * @param right The LargeNumber instance to divide by
     * @returns The LargeNumber instance that is the remainder of the left and right operands [Discards the quotient]
     * @private
     *
     */
    private static mod(left: LargeNumber, right: LargeNumber): LargeNumber {
        return this.remainder(left, right);
    }

    /**
     *
     * @param left The LargeNumber instance to divide
     * @param right The LargeNumber instance to divide by
     * @returns The LargeNumber instance that is the remainder of the left and right operands [Discards the quotient]
     * @private
     *
     */
    private static remainder(left: LargeNumber, right: LargeNumber): LargeNumber {
        return this.longDivisionWithRemainder(left, right)[1];
    }

    /**
     *
     * @param left The LargeNumber instance to divide
     * @param right The LargeNumber instance to divide by
     * @param precision The number of decimal places to round the final result to
     * @returns The LargeNumber instance that is the quotient of the left and right operands with the specified precision for decimal places
     * @private
     *
     */
    private static divide(left: LargeNumber, right: LargeNumber, precision: number): LargeNumber {
        const isFinalResultNegative = left.isNegative !== right.isNegative;

        left = left.abs();
        right = right.abs();

        if (right.equals(ParseLargeNumber(0))) {
            throw new Error('Cannot divide by zero');
        }
        if (left.equals(ParseLargeNumber(0))) {
            return ParseLargeNumber(0);
        }
        if (right.equals(ParseLargeNumber(1))) {
            return left.round(precision);
        }
        if (right.equals(left)) {
            return ParseLargeNumber(1);
        }

        const [adjustedLeft, adjustedRight] = LargeNumber.adjustNumeralsToRemoveDecimalPoint(left.value, right.value);
        let quotient = "";
        let currentDividend = ""
        const divisor = ParseLargeNumber(adjustedRight);
        let decimalCount = -1;
        for (let i = 0;; i++) {
            currentDividend += adjustedLeft[i] || '0';
            if (ParseLargeNumber(currentDividend).isGreaterThanOrEqual(divisor)) {
                const [currentQuotient, currentRemainder] = LargeNumber.bruteDivide(ParseLargeNumber(currentDividend), divisor);
                quotient = quotient + currentQuotient.value.split('.')[0];
                currentDividend = currentRemainder.value.split('.')[0];
            } else {
                if (i >= adjustedLeft.length - 1) {
                    if (quotient.includes('.')) {
                        quotient = quotient + '0'
                    } else {
                        quotient = quotient + '.'
                    }
                } else {
                    quotient = quotient + '0';
                }
            }
            if (quotient.includes('.')) {
                decimalCount++;
            }
            if (decimalCount === precision + 1 || (i >= adjustedLeft.length - 1 && (currentDividend === "0" || currentDividend === ""))) {
                break;
            }
        }
        return ParseLargeNumber(quotient).round(precision);
    }

    /**
     *
     * @param decimal The decimal number to convert to fraction
     * @returns An array with the first element being the numerator and the second element being the denominator
     * @private
     *
     */
    private static decimalToFraction(decimal: LargeNumber): [LargeNumber, LargeNumber] {
        const decimalAsString = !decimal.hasDecimalPoint() ? decimal.value.split('.')[0] : decimal.value;
        const decimalPlaces = decimal.hasDecimalPoint() ? decimal.value.split('.')[1].length : 0;
        const numerator = ParseLargeNumber(decimalAsString.replace('.', ''));
        const denominator = ParseLargeNumber(10).power(ParseLargeNumber(decimalPlaces));
        return [numerator, denominator];
    }

    /**
     *
     * @param base The base number
     * @param exponent The exponent number
     * @returns The LargeNumber instance that is the result of the base number raised to the power of the exponent number
     * @private
     *
     */
    private static power(base: LargeNumber, exponent: LargeNumber): LargeNumber {
        if(exponent.equals(ParseLargeNumber(0))) {
            return ParseLargeNumber(1);
        }
        if(base.equals(ParseLargeNumber(0))) {
            return ParseLargeNumber(0);
        }
        if(base.equals(ParseLargeNumber(1))) {
            return ParseLargeNumber(1);
        }
        if(exponent.equals(ParseLargeNumber(1))) {
            return base;
        }
        if(exponent.isLessThan(ParseLargeNumber(0))) {
            return ParseLargeNumber(1).divide(base.power(exponent.negate()));
        }
        if(exponent.hasDecimalPoint()) {
            const [exponentNumerator, exponentDenominator] = LargeNumber.decimalToFraction(exponent);
            return LargeNumber.power(base, exponentNumerator).root(exponentDenominator);
        }

        let result = ParseLargeNumber(1);
        for(let i = 0; ParseLargeNumber(i).isLessThan(exponent); i++) {
            result = result.multiply(base);
        }
        return result;
    }

    /**
     *
     * @param base The base number
     * @param root The root number
     * @returns The LargeNumber instance that is the result of the base number raised to the power of 1/root number
     * @private
     *
     */
    private static root(base: LargeNumber, root: LargeNumber): LargeNumber {
        if(base.isNegative) {
            throw new Error('Base must be greater than or equal to 0');
        }
        if(root.equals(ParseLargeNumber(0))) {
            throw new Error('Root must be greater than 0');
        }
        if(base.equals(ParseLargeNumber(0))) {
            return ParseLargeNumber(0);
        }
        if(base.equals(ParseLargeNumber(1))) {
            return ParseLargeNumber(1);
        }
        if(root.equals(ParseLargeNumber(1))) {
            return base;
        }
        if(root.isLessThan(ParseLargeNumber(0))) {
            return ParseLargeNumber(1).divide(base.root(root.negate()));
        }
        if(root.hasDecimalPoint()) {
            const [rootNumerator, rootDenominator] = LargeNumber.decimalToFraction(root);
            return LargeNumber.power(base, rootDenominator).root(rootNumerator);
        }

        let lowerBound = ParseLargeNumber(0);
        let upperBound = base;
        let midPoint = base.divideWithPrecision(10, ParseLargeNumber(2));
        let midPointToPowerOfRoot = midPoint.power(root);
        // todo: Complete
        return ParseLargeNumber(0);
    }
}



export default ParseLargeNumber;
