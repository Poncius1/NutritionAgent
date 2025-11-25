function RadioGroup({ label, helperText, name, options, value, onChange }) {
  return (
    <div className="space-y-1 col-span-1 md:col-span-2">
      <p className="text-sm font-medium text-gray-700">{label}</p>
      {helperText && (
        <p className="text-xs text-gray-400 mb-1">{helperText}</p>
      )}

      <div className="flex flex-wrap gap-3">
        {options.map((option) => {
          const id = `${name}-${option.value}`;
          const isSelected = value === option.value;
          return (
            <label
              key={option.value}
              htmlFor={id}
              className={[
                "flex items-center gap-2 px-3 py-2 rounded-lg border cursor-pointer text-sm",
                isSelected
                  ? "border-nutrition-blue bg-nutrition-blue/5 text-nutrition-darkBlue"
                  : "border-gray-300 text-gray-600 hover:border-nutrition-blue/60",
              ].join(" ")}
            >
              <input
                id={id}
                type="radio"
                name={name}
                value={option.value}
                checked={isSelected}
                onChange={(e) => onChange(e.target.value)}
                className="h-4 w-4 text-nutrition-blue focus:ring-nutrition-blue"
              />
              <span>{option.label}</span>
            </label>
          );
        })}
      </div>
    </div>
  );
}

export default RadioGroup;