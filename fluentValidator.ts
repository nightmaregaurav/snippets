export class Ensure<T> {
    private readonly parent?: Ensure<any>;
    private readonly value: T;
    private readonly errors: string[];

    constructor(value: T, parent?: Ensure<any>) {
        if (parent){
            this.parent = parent;
            this.errors = parent.errors;
        } else {
            this.errors = [];
        }
        this.value = value;
    }

    public static given<T>(value: T): Ensure<T> {
        return new Ensure<T>(value);
    }

    public peek<TT>(transform: (value: T) => TT): Ensure<TT> {
        const newValue = transform(this.value);
        return new Ensure<TT>(newValue, this);
    }

    public passesTest(testName: string, test: (value: T) => boolean): Ensure<T> {
        if (!test(this.value)) {
            this.errors.push(`Value must pass test "${testName}".`);
        }
        return this;
    }

    public isNullish(): Ensure<T> {
        if (this.value !== null && this.value !== undefined) {
            this.errors.push('Value must be null or undefined.');
        }
        return this;
    }

    public isNotNullish(): Ensure<T> {
        if (this.value === null || this.value === undefined) {
            this.errors.push('Value must not be null or undefined.');
        }
        return this;
    }

    public isString(): Ensure<T> {
        if (typeof this.value !== 'string') {
            this.errors.push('Value must be a string.');
        }
        return this;
    }

    public isNotString(): Ensure<T> {
        if (typeof this.value === 'string') {
            this.errors.push('Value must not be a string.');
        }
        return this;
    }

    public isNumeric(): Ensure<T> {
        if (typeof this.value !== 'string'){
            throw Error("isNumeric can only be applied to strings.");
        }
        if (!/^-?\d*\.?\d+$/.test(this.value)) {
            this.errors.push('Value must be numeric.');
        }
        return this;
    }

    public isNotNumeric(): Ensure<T> {
        if (typeof this.value !== 'string') {
            throw Error("isNotNumeric can only be applied to strings.");
        }

        if (/^-?\d*\.?\d+$/.test(this.value)) {
            this.errors.push('Value must not be numeric.');
        }
        return this;
    }

    public isNumber(): Ensure<T> {
        if (typeof this.value !== 'number') {
            this.errors.push('Value must be a valid number.');
        }
        return this;
    }

    public isNotNumber(): Ensure<T> {
        if (typeof this.value === 'number') {
            this.errors.push('Value must not be a valid number.');
        }
        return this;
    }

    public isObject(): Ensure<T> {
        if (typeof this.value !== 'object' || this.value === null || Array.isArray(this.value)) {
            this.errors.push('Value must be an object.');
        }
        return this;
    }

    public isNotObject(): Ensure<T> {
        if (typeof this.value === 'object' && this.value !== null && !Array.isArray(this.value)) {
            this.errors.push('Value must not be an object.');
        }
        return this;
    }

    public isArray(): Ensure<T> {
        if (!Array.isArray(this.value)) {
            this.errors.push('Value must be an array.');
        }
        return this;
    }

    public isNotArray(): Ensure<T> {
        if (Array.isArray(this.value)) {
            this.errors.push('Value must not be an array.');
        }
        return this;
    }

    public isLessThan(limit: number | string): Ensure<T> {
        if (typeof this.value !== 'number' && typeof this.value !== 'string') {
            throw new Error('isLessThan can only be applied to numbers and strings.');
        }
        if (this.value >= limit) {
            this.errors.push(`Value must be less than ${limit}.`);
        }
        return this;
    }

    public isNotLessThan(limit: number | string): Ensure<T> {
        if (typeof this.value !== 'number' && typeof this.value !== 'string') {
            throw new Error('isNotLessThan can only be applied to numbers and strings.');
        }
        if (this.value < limit) {
            this.errors.push(`Value must not be less than ${limit}.`);
        }
        return this;
    }

    public isGreaterThan(limit: number | string): Ensure<T> {
        if (typeof this.value !== 'number' && typeof this.value !== 'string') {
            throw new Error('isGreaterThan can only be applied to numbers and strings.');
        }
        if (this.value <= limit) {
            this.errors.push(`Value must be greater than ${limit}.`);
        }
        return this;
    }

    public isNotGreaterThan(limit: number | string): Ensure<T> {
        if (typeof this.value !== 'number' && typeof this.value !== 'string') {
            throw new Error('isNotGreaterThan can only be applied to numbers and strings.');
        }
        if (this.value > limit) {
            this.errors.push(`Value must not be greater than ${limit}.`);
        }
        return this;
    }

    public startsWith(substring: string): Ensure<T> {
        if (typeof this.value !== 'string') {
            throw new Error('startsWith can only be applied to strings.');
        }
        if (!this.value.startsWith(substring)) {
            this.errors.push(`Value must start with the substring '${substring}'.`);
        }
        return this;
    }

    public doesNotStartWith(substring: string): Ensure<T> {
        if (typeof this.value !== 'string') {
            throw new Error('doesNotStartWith can only be applied to strings.');
        }
        if (this.value.startsWith(substring)) {
            this.errors.push(`Value must not start with the substring '${substring}'.`);
        }
        return this;
    }

    public endsWith(substring: string): Ensure<T> {
        if (typeof this.value !== 'string') {
            throw new Error('endsWith can only be applied to strings.');
        }
        if (!this.value.endsWith(substring)) {
            this.errors.push(`Value must end with the substring '${substring}'.`);
        }
        return this;
    }

    public doesNotEndWith(substring: string): Ensure<T> {
        if (typeof this.value !== 'string') {
            throw new Error('doesNotEndWith can only be applied to strings.');
        }
        if (this.value.endsWith(substring)) {
            this.errors.push(`Value must not end with the substring '${substring}'.`);
        }
        return this;
    }

    public equals(expectedValue: any): Ensure<T> {
        if (this.value !== expectedValue) {
            this.errors.push(`Value must be equal to ${expectedValue}.`);
        }
        return this;
    }

    public isNotEqual(expectedValue: any): Ensure<T> {
        if (this.value === expectedValue) {
            this.errors.push(`Value must not be equal to ${expectedValue}.`);
        }
        return this;
    }

    public matchesRegex(regex: RegExp): Ensure<T> {
        if (typeof this.value !== 'string') {
            throw new Error('matchesRegex can only be applied to strings.');
        }
        if (!regex.test(this.value)) {
            this.errors.push('Value does not match the expected format.');
        }
        return this;
    }

    public doesNotMatchRegex(regex: RegExp): Ensure<T> {
        if (typeof this.value !== 'string') {
            throw new Error('doesNotMatchRegex can only be applied to strings.');
        }
        if (regex.test(this.value)) {
            this.errors.push('Value must not match the expected format.');
        }
        return this;
    }

    public contains(value: T): Ensure<T> {
        if (typeof this.value !== 'string' && !Array.isArray(this.value)) {
            throw new Error('contains can only be applied to strings and arrays.');
        }
        if (typeof this.value !== typeof value) {
            throw new Error('contains can only be applied to same types.');
        }
        if (this.value.indexOf(value as any) === -1) {
            this.errors.push(`Value must contain '${value}'.`);
        }
        return this;
    }

    public doesNotContain(value: T): Ensure<T> {
        if (typeof this.value !== 'string' && !Array.isArray(this.value)) {
            throw new Error('doesNotContain can only be applied to strings and arrays.');
        }
        if (typeof this.value !== typeof value) {
            throw new Error('doesNotContain can only be applied to same types.');
        }
        if (this.value.indexOf(value as any) !== -1) {
            this.errors.push(`Value must not contain '${value}'.`);
        }
        return this;
    }

    public hasLength(length: number): Ensure<T> {
        if (typeof this.value !== 'string' && !Array.isArray(this.value)) {
            throw new Error('hasLength can only be applied to strings and arrays.');
        }
        if (this.value.length !== length) {
            this.errors.push(`Value must have a length of ${length}.`);
        }
        return this;
    }

    public doesNotHaveLength(length: number): Ensure<T> {
        if (typeof this.value !== 'string' && !Array.isArray(this.value)) {
            throw new Error('doesNotHaveLength can only be applied to strings and arrays.');
        }
        if (this.value.length === length) {
            this.errors.push(`Value must not have a length of ${length}.`);
        }
        return this;
    }

    public hasAtLeastLength(length: number): Ensure<T> {
        if (typeof this.value !== 'string' && !Array.isArray(this.value)) {
            throw new Error('hasAtLeastLength can only be applied to strings and arrays.');
        }
        if (this.value.length >= length) {
            this.errors.push(`Value must have a length of ${length} at minimum.`);
        }
        return this;
    }

    public hasAtMostLength(length: number): Ensure<T> {
        if (typeof this.value !== 'string' && !Array.isArray(this.value)) {
            throw new Error('hasAtMostLength can only be applied to strings and arrays.');
        }
        if (this.value.length <= length) {
            this.errors.push(`Value must have a length of ${length} at maximum.`);
        }
        return this;
    }

    public evaluate(): { isValid: boolean; errors: string[] } {
        return {isValid: this.errors.length === 0, errors: this.errors};
    }
}
