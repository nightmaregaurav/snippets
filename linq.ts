type Predicate<T> = (item: T) => boolean;
type Selector<TSource, TResult> = (item: TSource) => TResult;
type Comparer<T> = (a: T, b: T) => number;
type KeySelector<TSource, TKey> = (item: TSource) => TKey;

class Linq<T> {
    private readonly data: T[];

    constructor(data: T[]) {
        this.data = data;
    }

    where(predicate: Predicate<T>): Linq<T> {
        const filteredData: T[] = [];
        for (const item of this.data) {
            if (predicate(item)) {
                filteredData.push(item);
            }
        }
        return new Linq<T>(filteredData);
    }

    select<TResult>(selector: Selector<T, TResult>): Linq<TResult> {
        const projectedData: TResult[] = [];
        for (const item of this.data) {
            projectedData.push(selector(item));
        }
        return new Linq<TResult>(projectedData);
    }

    orderBy(comparer: Comparer<T>): Linq<T> {
        const sortedData = [...this.data].sort(comparer);
        return new Linq<T>(sortedData);
    }

    groupBy<TKey>(keySelector: KeySelector<T, TKey>): Map<TKey, T[]> {
        const groups = new Map<TKey, T[]>();
        for (const item of this.data) {
            const key = keySelector(item);
            if (!groups.has(key)) {
                groups.set(key, []);
            }
            groups.get(key)!.push(item);
        }
        return groups;
    }

    join<TInner, TKey, TResult>(
        inner: TInner[],
        outerKeySelector: KeySelector<T, TKey>,
        innerKeySelector: KeySelector<TInner, TKey>,
        resultSelector: (outer: T, inner: TInner) => TResult
    ): Linq<TResult> {
        const joinedData: TResult[] = [];
        for (const outerItem of this.data) {
            const outerKey = outerKeySelector(outerItem);
            for (const innerItem of inner) {
                const innerKey = innerKeySelector(innerItem);
                if (outerKey === innerKey) {
                    const result = resultSelector(outerItem, innerItem);
                    joinedData.push(result);
                }
            }
        }
        return new Linq<TResult>(joinedData);
    }

    intersect(other: T[]): Linq<T> {
        const intersectedData = this.data.filter(item => other.includes(item));
        return new Linq<T>(intersectedData);
    }

    except(other: T[]): Linq<T> {
        const exceptedData = this.data.filter(item => !other.includes(item));
        return new Linq<T>(exceptedData);
    }

    include(...items: T[]): Linq<T> {
        const includedData = [...this.data, ...items];
        return new Linq<T>(includedData);
    }

    forEach(action: (item: T) => void): void {
        for (const item of this.data) {
            action(item);
        }
    }

    all(predicate: Predicate<T>): boolean {
        for (const item of this.data) {
            if (!predicate(item)) {
                return false;
            }
        }
        return true;
    }

    any(predicate?: Predicate<T>): boolean {
        if (predicate) {
            for (const item of this.data) {
                if (predicate(item)) {
                    return true;
                }
            }
            return false;
        } else {
            return this.data.length > 0;
        }
    }

    count(predicate?: Predicate<T>): number {
        if (predicate) {
            return this.data.filter(predicate).length;
        } else {
            return this.data.length;
        }
    }

    isEmpty(): boolean {
        return this.data.length === 0;
    }

    isNotEmpty(): boolean {
        return !this.isEmpty();
    }

    skip(count: number): Linq<T> {
        return new Linq<T>(this.data.slice(count));
    }

    skipWhile(predicate: Predicate<T>): Linq<T> {
        let i = 0;
        while (i < this.data.length && predicate(this.data[i])) {
            i++;
        }
        return new Linq<T>(this.data.slice(i));
    }

    take(count: number): Linq<T> {
        return new Linq<T>(this.data.slice(0, count));
    }

    takeWhile(predicate: Predicate<T>): Linq<T> {
        let i = 0;
        while (i < this.data.length && predicate(this.data[i])) {
            i++;
        }
        return new Linq<T>(this.data.slice(0, i));
    }

    distinct(): Linq<T> {
        const distinctData = Array.from(new Set(this.data));
        return new Linq<T>(distinctData);
    }

    reverse(): Linq<T> {
        const reversedData = [...this.data].reverse();
        return new Linq<T>(reversedData);
    }

    first(predicate?: Predicate<T>): T {
        if (predicate) {
            const foundItem = this.data.find(predicate);
            if (foundItem === undefined) {
                throw new Error("Element not found.");
            }
            return foundItem;
        } else {
            if (this.data.length === 0) {
                throw new Error("Element not found.");
            }
            return this.data[0];
        }
    }

    firstOrDefault(predicate?: Predicate<T>): T | null {
        if (predicate) {
            return this.data.find(predicate) || null;
        } else {
            return this.data.length > 0 ? this.data[0] : null;
        }
    }

    last(predicate?: Predicate<T>): T {
        if (predicate) {
            const reversedData = this.data.slice().reverse();
            const foundItem = reversedData.find(predicate);
            if (foundItem === undefined) {
                throw new Error("Element not found.");
            }
            return foundItem;
        } else {
            if (this.data.length === 0) {
                throw new Error("Element not found.");
            }
            return this.data[this.data.length - 1];
        }
    }

    lastOrDefault(predicate?: Predicate<T>): T | null {
        if (predicate) {
            const reversedData = this.data.slice().reverse();
            return reversedData.find(predicate) || null;
        } else {
            return this.data.length > 0 ? this.data[this.data.length - 1] : null;
        }
    }

    single(predicate?: Predicate<T>): T {
        if (predicate) {
            const foundItems = this.data.filter(predicate);
            if (foundItems.length !== 1) {
                throw new Error("Expected exactly one element.");
            }
            return foundItems[0];
        } else {
            if (this.data.length !== 1) {
                throw new Error("Expected exactly one element.");
            }
            return this.data[0];
        }
    }

    singleOrDefault(predicate?: Predicate<T>): T | null {
        if (predicate) {
            const foundItems = this.data.filter(predicate);
            return foundItems.length === 1 ? foundItems[0] : null;
        } else {
            return this.data.length === 1 ? this.data[0] : null;
        }
    }

    elementAt(index: number): T {
        if (index < 0 || index >= this.data.length) {
            throw new Error("Index out of range.");
        }
        return this.data[index];
    }

    elementAtOrDefault(index: number): T | null {
        return index >= 0 && index < this.data.length ? this.data[index] : null;
    }

    min(comparer?: Comparer<T>): T | null {
        if (this.data.length === 0) {
            return null;
        }
        if (comparer) {
            return this.data.slice().sort(comparer)[0];
        } else {
            return this.data.slice().sort()[0];
        }
    }

    max(comparer?: Comparer<T>): T | null {
        if (this.data.length === 0) {
            return null;
        }
        if (comparer) {
            return this.data.slice().sort(comparer)[this.data.length - 1];
        } else {
            return this.data.slice().sort()[this.data.length - 1];
        }
    }

    sum(selector?: Selector<T, number>): number {
        if (this.data.length === 0) {
            return 0;
        }
        if (selector) {
            return this.data.reduce((sum, item) => sum + selector(item), 0);
        } else {
            return this.data.reduce((sum, item) => sum + (item as any), 0);
        }
    }

    average(selector?: Selector<T, number>): number | null {
        if (this.data.length === 0) {
            return null;
        }
        const sum = selector
            ? this.data.reduce((sum, item) => sum + selector(item), 0)
            : this.data.reduce((sum, item) => sum + (item as any), 0);
        return sum / this.data.length;
    }

    toDictionary<TKey>(
        keySelector: Selector<T, TKey>,
        valueSelector?: Selector<T, any>
    ): Map<TKey, T | any> {
        const dictionary = new Map<TKey, T | any>();
        for (const item of this.data) {
            const key = keySelector(item);
            const value = valueSelector ? valueSelector(item) : item;
            dictionary.set(key, value);
        }
        return dictionary;
    }

    defaultIfEmpty(defaultValue: T): Linq<T> {
        return this.data.length === 0 ? new Linq<T>([defaultValue]) : this;
    }

    zip<TInner, TResult>(
        inner: TInner[],
        resultSelector: (outer: T, inner: TInner) => TResult
    ): Linq<TResult> {
        const zippedData: TResult[] = [];
        const length = Math.min(this.data.length, inner.length);
        for (let i = 0; i < length; i++) {
            const result = resultSelector(this.data[i], inner[i]);
            zippedData.push(result);
        }
        return new Linq<TResult>(zippedData);
    }

    sequenceEqual(other: T[]): boolean {
        if (this.data.length !== other.length) {
            return false;
        }
        for (let i = 0; i < this.data.length; i++) {
            if (this.data[i] !== other[i]) {
                return false;
            }
        }
        return true;
    }

    distinctBy<TKey>(keySelector: Selector<T, TKey>): Linq<T> {
        const distinctData = new Map<TKey, T>();
        for (const item of this.data) {
            const key = keySelector(item);
            if (!distinctData.has(key)) {
                distinctData.set(key, item);
            }
        }
        return new Linq<T>(Array.from(distinctData.values()));
    }

    toArray(): T[] {
        return this.data;
    }
}
